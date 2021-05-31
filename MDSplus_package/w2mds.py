# Write UEDGE variables and derived quantities to MDSplus
#
# modification history:
#	22 Aug 2006	Created, starting with rewrite_uedge2mds [GDP]
#	29 Aug 2006	Added Psin description to /snapshot.grid [GDP]
#	30 Aug 2006	replaced nsm1=com.nhsp with nsm1=2*com.nhgsp
#	10 Oct 2006	corrected problems identified by Coster [GDP]
#	26 Mar 2007	added DSTARG parameters
#	25 Jan 2021	Translated into Python for PyUedge. Uses the MDSPlus
#                       thick client. [WM]
#   21 May 2021 Translation to Python completed [AH]
#

global version
version = '0.1 21 May 21 - AH'

def exists(model, shot):
    ''' Checks whether shot of tree 'model' exists'''
    try: 
        tree.Tree(model,shot,'EDIT')
        outtree.close()
        return True
    except:
        return False

def with_unit(data, unit):
    from MDSplus import BUILD_WITH_UNITS
    return BUILD_WITH_UNITS(data,unit)

def new_tree(model, shot = None, verbose=False):
    ''' Creates a new shot to the tree 'model'
    
    Parameters
    ----------
    model : str
        string for model tree to be created. model_path must exist
        as an environment variable upon creation
    shot : int (default: None)
        tries to create the new tree with shot number defined by shot.
        If shot is not none, the current shot will not be increased
    '''
    from MDSplus import tree

    # If no shot is requested, assign next free shot 
    if shot is None: 
        outtree = tree.Tree(model)
        shot = outtree.incrementCurrent()
        outtree.close()

    if exists(model, shot):
        if verbose:
            print("Current shot ",shot,", already exists. Aborting.")
        return False
    else:
        if verbose:
           print("Writing to shot {}".format(shot))
    outtree = tree.Tree(model)
    outtree.createPulse(shot)
    outtree = tree.Tree(model,shot,'EDIT')

    return outtree

def find_iximp():
    ''' Returns the poloidal index of ixmp based on proximity to mag Z-axis'''
    from uedge import com
    from numpy import where

    LHS = abs(com.zm[:,:,0] - com.zmagx)[:int(0.5*(com.ixpt1[0]+com.ixpt2[0]))]
    return where( LHS == LHS.min())[0][0]

def calc_xlength():
    ''' Calculates the poloidal and parallel distance from the IT '''
    from uedge import com
    from numpy import zeros

    dcc = 0.5/com.gx # Distance from face to cell center
    dc = 1/com.gx # Distance over cell
    
    [xpol, xpar] = [zeros((com.nx + 2, com.ny + 2)) for i in range(2)]
    xpol[0] = - dc[0]

    polcore = sum(dc[com.ixpt1[0]+1:com.ixpt2[0]+1])
    parcore = sum(dc[com.ixpt1[0]+1:com.ixpt2[0]+1]
                    /com.rr[com.ixpt1[0]+1:com.ixpt2[0]+1])
    for i in range(1,com.nx + 2):
        xpol[i] = sum(dc[1:i]) + dcc[i]
        xpar[i] = sum(dc[1:i]/com.rr[1:i]) + dcc[i]/com.rr[i]
        # Account for closed flux surfaces in the core
        if (i>com.ixpt1[0]) and (i<=com.ixpt2[0]):
            xpol[i,:com.iysptrx+1], xpar[i,:com.iysptrx+1] = 0, 0
        # Account for the PFR being adjoint of the core
        if i>com.ixpt2[0]:
            xpol[i,:com.iysptrx+1] -= polcore[:com.iysptrx+1]
            xpar[i,:com.iysptrx+1] -= parcore[:com.iysptrx+1]


    return xpol, xpar

def calc_ylength():
    ''' Calculates the radial distance from the separatrix '''
    from numpy import zeros, sum
    from uedge import com

    dcc = 0.5/com.gy
    dc = 1/com.gy
    
    lrad = zeros((com.nx+2, com.ny+2))
    lsep = sum(dc[:,:com.iysptrx+1], axis=1) # Radial location of separatrix
    for iy in range(com.ny+2):
        lrad[:,iy] = sum(dc[:,:iy], axis=1) + dcc[:,iy] - lsep

    return lrad

def make_regvol():
    ''' Calculates a marking matrix for the different grid regions'''
    from uedge import com
    from numpy import zeros
 
    # TODO: DN-case?
    # Range upper bound is exclusive: +1 to upper bound
    corex = slice((int)(com.ixpt1[0]+1),(int)(com.ixpt2[0]+1)) # Core X-coords
    lpfrx = slice(0,(int)(com.ixpt1[0]+1)) # Left PFR x-coords
    rpfrx = slice((int)(com.ixpt2[0]+1),(int)(com.nx + 2)) # Right PFR x-coords
    private = slice(0,(int)(com.iysptrx+1)) # Private flux y-coords
    common = slice((int)(com.iysptrx+1),(int)(com.ny + 2)) # Common flux y-coords

    regvol = zeros((com.nx + 2, com.ny + 2),dtype=int) # AH - full domain (GCs incl)
    regvol[corex,private] = 1 # Mark core region as 1
    regvol[corex,common] = 2 # Mark Common SOL Core region as 2
    regvol[lpfrx,:] = 3 # Mark left PFR region as 3
    regvol[rpfrx,:] = 4 # Mark right PFR as 4

    return regvol



def make_fluidarray(ionarr, neutarr, label=False):
    ''' Creates an array containing all fluid species parameters '''
    # NOTE: Ordered by Z, atoms - ions within Z, molecules last
    from uedge import bbb, com
    from numpy import argsort, zeros 

    # order[0] flags ion (<0) or neutral (=0), order[1] the index in the array
    order = []
    # Species symbols for species labels
    isotope = ['', 'H', 'D', 'T'] 
    sym = ['','X','He','Li','Be','B','C','N','O','F','Ne']
    if label:
        order.append(sym[1]+'0')
        order.append(sym[1]+'+')
    else:
        # First, add neutral hydrogenic species
        if bbb.isupgon[0] == 1:
            order.append([-1, 1])
        else:
            order.append([0, 0])
        # Then, add ionic hydrogenic species
        order.append([-1, 0])
    # Then, add any impurities
    ngzsp = sum(com.nzsp>0) # Number of impurity species
    nizsp = sum(com.nzsp) # Number of ion species
    imps = [] # Temporary list for ordering
    ind = 1*(bbb.isupgon[0] == 1) # Ion index flag
    # First, we store the list and positions
    if ngzsp>0: # Impurities are present
        for i in range(ngzsp): # Loop through each impurity species
            buff = [] # Buffer list
            if label:
                buff.append('{}0'.format(sym[com.nzsp[i]]))
            else:
                buff.append([0, 1 + bbb.ishymol + i]) # Add neutrals
            for j in range(com.nzsp[i]):
                ind += 1 # Keep track of location in array
                if label:
                    buff.append('{}{}+'.format(sym[com.nzsp[i]],
                                    (j>0)*('{}'.format(j+1))))
                else:
                    buff.append([-1, ind])
            imps.append(buff) # Add the whole impurity package
        # Order imps by Z, and add to array
        for i in argsort(com.nzsp[:ngzsp]):
            for j in imps[i]:
                order.append(j)
    # Finally, add the molecules last, if they are present
    if bbb.ishymol:
        if label:
            order.append(sym[1]+'2')
        else:
            order.append([0, 1])
    # Finally, compile the new list
    # NOTE: assume the input arrays to always have the 
    # species as the last dimension
    if label:
        ret = []
        for i in order:
            ret.append(i.replace('X',isotope[int(bbb.minu[0])]))
    elif len(ionarr.shape) == 1: # Integer/Char array
        ret = zeros((len(order)))
        for i in range(len(order)):
            if order[i][0]<0:
                ret[i] = ionarr[order[i][1]]
            else:
                ret[i] = neutarr[order[i][1]]
    elif len(ionarr.shape) == 2: # List of arrays
        ret = zeros((ionarr.shape[0], len(order)))
        for i in range(len(order)):
            if order[i][0]<0:
                ret[:,i] = ionarr[:,order[i][1]]
            else:
                ret[:,i] = neutarr[:,order[i][1]]
    elif len(ionarr.shape) == 3: # List of arrays
        ret = zeros((ionarr.shape[0], ionarr.shape[1], len(order)))
        for i in range(len(order)):
            if order[i][0]<0:
                ret[:,:,i] = ionarr[:,:,order[i][1]]
            else:
                ret[:,:,i] = neutarr[:,:,order[i][1]]
    return ret
 

def store_snapshot_dimensions(tree):
    ''' Writes data to node SNAPSHOT.DIMENSIONS of tree''' 
    from uedge import com, bbb, grd

    snpsdim = tree.SNAPSHOT.DIMENSIONS # Variable pointing to SNAPHSOT.DIMENSIONS
    inertial = (bbb.isupgon[0]==1)
    # Write UEDGE variables and derived quantities to MDSplus

    # Inner midplane location
    snpsdim.IMP.putData(find_iximp())
    snpsdim.IMP.BASISNAME.putData("From find_iximp: ~(ixpt1+1+ixptop]/2")
    snpsdim.IMP.COMMENT.putData("Poloidal index of IMP")
    
    # Number of atomic species
    snpsdim.NATM.putData(int(com.ngsp-bbb.ishymol))
    snpsdim.NATM.BASISNAME.putData('com.ngsp-bbb.ishymol')
    snpsdim.NATM.COMMENT.putData('Number of atomic species')

    # place holder for Coster's NION parameter, number of test ion species
    # AH 5/21
    snpsdim.NION.putData(int(com.nisp-bbb.isupgon[0]))
    snpsdim.NION.BASISNAME.putData('com.nisp-bbb.isupgon[0]')
    snpsdim.NION.COMMENT.putData('Number of charged species in the simulation')

    # place holder for Coster's NMOL parameter, number of molecular species
    # AH 5/21
    snpsdim.NMOL.putData(int(bbb.ishymol))
    snpsdim.NMOL.BASISNAME.putData('bbb.ishymol')
    snpsdim.NMOL.COMMENT.putData('Number of molecular species in simulation')

    # Number of fluid species: UEDGE treats D and Imp atoms as fluid species! 
    snpsdim.NS.putData(int(com.nisp+com.ngsp-1*inertial))
    snpsdim.NS.BASISNAME.putData('Inertial atoms: '*inertial + 
                'Diffusive atoms: '*(not inertial) + 'com.nisp+com.ngsp'+ 
                '-1'*inertial)
    snpsdim.NS.COMMENT.putData('Number of fluid species in simulation')

    # Number of cells in poloidal direction, including guard cells
    snpsdim.NX.putData(com.nx+2)
    snpsdim.NX.BASISNAME.putData('com.nx+2')
    snpsdim.NX.COMMENT.putData('Number of cells in the poloidal direction')

    # Number of cells in radial directions, including guard cells
    snpsdim.NY.putData(com.ny+2)
    snpsdim.NY.BASISNAME.putData("com.ny+2")
    snpsdim.NY.COMMENT.putData('Number of cells in the radial direction')

    # Index of the outer midplane
    snpsdim.OMP.putData(bbb.ixmp)
    snpsdim.OMP.BASISNAME.putData('bbb.ixmp')
    snpsdim.OMP.COMMENT.putData('Poloidal index of OMP')

    # Index of the separatrix
    snpsdim.SEP.putData(com.iysptrx)
    snpsdim.SEP.BASISNAME.putData('com.iysptrx')
    snpsdim.SEP.COMMENT.putData('Index of last flux tube inside the '+
                                'separatrix')

    # Index of the target 1 
    snpsdim.TARG1.putData(com.ixlb[0])
    snpsdim.TARG1.BASISNAME.putData('com.ixlb[0]')
    snpsdim.TARG1.COMMENT.putData('Index of target 1: staggered' + 
                ' parameters.\nFor cell-center, non-staggered parameters,' +
                ' add 1')


    # Index of the target 2 [for snull]
    snpsdim.TARG2.putData(com.ixrb[0])
    snpsdim.TARG2.BASISNAME.putData('com.ixrb[0]')
    snpsdim.TARG2.COMMENT.putData('Index of target 4: staggered' + 
                ' and cell center parameters.')

    # Double-null targets
    # TODO: DN dimensions not yet fully implemented/verified!
    if com.nxpt == 2:

        # Index of the target 2 [for DN]
        snpsdim.TARG2.putData(com.ixrb[0])
        snpsdim.TARG2.BASISNAME.putData('com.ixrb[0]')
        snpsdim.TARG2.COMMENT.putData('Index of target 2: staggered' + 
                ' and cell center parameters.')
        
       # Index of the target 3
        snpsdim.TARG3.putData(com.ixlb[1])
        snpsdim.TARG3.BASISNAME.putData('com.ixlb[1]')
        snpsdim.TARG3.COMMENT.putData('Index of target 3: staggered' + 
                ' parameters.\nFor cell-center, non-staggered parameters,' +
                ' add 1')

       # Index of the target 4 [if DN]
        snpsdim.TARG4.putData(com.ixrb[1])
        snpsdim.TARG4.BASISNAME.putData('com.ixrb[1]')
        snpsdim.TARG4.COMMENT.putData('Index of target 4: staggered' + 
                ' and cell center parameters.')

    return True

def store_snapshot_grid(tree):
    ''' Writes data to node SNAPSHOT.GRID of tree '''
    from numpy import zeros, array
    from uedge import bbb, com

    
    snpsgrd = tree.SNAPSHOT.GRID # Variable pointing to SNAPHSOT.DIMENSIONS

    # Species mass
    am = make_fluidarray(bbb.minu, bbb.mg/bbb.mp)
    snpsgrd.AM.putData(array(am))
    snpsgrd.AM.BASISNAME.putData('make_fluidarray(bbb.mg[0]/bbb.mp, bbb.minu)')
    snpsgrd.AM.COMMENT.putData('Atom/ion fluid species mass [amu]')
    

    # Generate UEDGE variables for rightix, leftix, etc.
    # NOTE: Assume these to be defining cell neighbors in each direction!
    [rightix, leftix, topix, bottomix, leftiy, rightiy, topiy, bottomiy] = \
    [zeros((com.nx + 2, com.ny + 2), dtype=int) for i in range(8)]

    rightix = bbb.ixp1
    leftix = bbb.ixm1
    for ix in range(com.nx + 2):
        topix[ix] = ix
        bottomix[ix] = ix

    for iy in range(com.ny + 2):
        topiy[:,iy] = min(iy+1, com.ny + 1)
        bottomiy[:,iy] = max(iy-1, 0)
        leftiy[:,iy] = iy
        rightiy[:,iy] = iy

    
    snpsgrd.RIGHTIX.putData(rightix)
    snpsgrd.RIGHTIX.BASISNAME.putData('bbb.ixp1')
    snpsgrd.RIGHTIX.COMMENT.putData('RHS cell neighbor poloidal index')

    snpsgrd.LEFTIX.putData(leftix)
    snpsgrd.LEFTIX.BASISNAME.putData('bbb.ixm1')
    snpsgrd.LEFTIX.COMMENT.putData('LHS cell neighbor poloidal index')

    snpsgrd.TOPIX.putData(topix)
    snpsgrd.TOPIX.BASISNAME.putData('ix')
    snpsgrd.TOPIX.COMMENT.putData('Top cell neighbor poloidal index')

    snpsgrd.BOTTOMIX.putData(bottomix)
    snpsgrd.BOTTOMIX.BASISNAME.putData('ix')
    snpsgrd.BOTTOMIX.COMMENT.putData('Bottom cell neighbor poloidal index')

    snpsgrd.TOPIY.putData(topiy)
    snpsgrd.TOPIY.BASISNAME.putData('min(iy, nx + 1)')
    snpsgrd.TOPIY.COMMENT.putData('Top cell neighbor radial index')

    snpsgrd.BOTTOMIY.putData(bottomiy)
    snpsgrd.BOTTOMIY.BASISNAME.putData('max(iy, 0)')
    snpsgrd.BOTTOMIY.COMMENT.putData('Bottom cell neighbor radial index')

    snpsgrd.LEFTIY.putData(leftiy)
    snpsgrd.LEFTIY.BASISNAME.putData('iy')
    snpsgrd.LEFTIY.COMMENT.putData('LHS cell neighbor radial index')

    snpsgrd.RIGHTIY.putData(rightiy)
    snpsgrd.RIGHTIY.BASISNAME.putData('iy')
    snpsgrd.RIGHTIY.COMMENT.putData('RHS cell neighbor radial index')

    # R- coordinate of cell centers, Z in machine coordinates
    snpsgrd.CR.putData(with_unit(com.rm,'m'))
    snpsgrd.CR.BASISNAME.putData('com.rm')
    snpsgrd.CR.COMMENT.putData('Radial coordinate of cell vertices. 3rd '+
        'dimension order: CC, SW, SE, NW, NE')

    # normalized poloidal flux of each cell
    snpsgrd.PSIN.putData((com.psi[:,:,0]-com.simagx)/(com.sibdry-com.simagx))
    snpsgrd.PSIN.BASISNAME.putData('(com.psi[:,:,0]-com.simagx)/'+
                                    '(com.sibdry-com.simagx)')
    snpsgrd.PSIN.COMMENT.putData('Normalied poloidal flux at cell center')


    # R- and Z-coordinate of cell east [X] face, Z in machine coordinates
    snpsgrd.CR_X.putData(with_unit(0.5*sum(com.rm[:,:,slice(2,4)]),'m'))
    snpsgrd.CR_X.BASISNAME.putData('0.5*sum(com.rm[:,:,slice(2,4)])')
    snpsgrd.CR_X.COMMENT.putData('Radial coordinate of poloidal east face')

    snpsgrd.CZ_X.putData(with_unit(0.5*sum(com.zm[:,:,slice(2,4)]-
                                com.zshift),'m'))
    snpsgrd.CZ_X.BASISNAME.putData('0.5*sum(com.rm[:,:,slice(2,4)])'+
                                '-com.zshift')
    snpsgrd.CZ_X.COMMENT.putData('Vertical coordinate of poloidal east face')

    # R- and Z-coordinate of cell north [Y] face, Z in machine coordinates
    snpsgrd.CR_Y.putData(with_unit(0.5*sum(com.rm[:,:,slice(3,4)]),'m'))
    snpsgrd.CR_Y.BASISNAME.putData('0.5*sum(com.rm[:,:,slice(3,4)])')
    snpsgrd.CR_Y.COMMENT.putData('Radial coordinate of poloidal north face')

    snpsgrd.CZ_Y.putData(with_unit(0.5*sum(com.zm[:,:,slice(3,4)]),'m'))
    snpsgrd.CZ_Y.BASISNAME.putData('0.5*sum(com.zm[:,:,slice(3,4)])')
    snpsgrd.CZ_Y.COMMENT.putData('Vertical coordinate of poloidal north face')

    lpol, lpar = calc_xlength()    

    # Parallel distance
    snpsgrd.DSPAR.putData(with_unit(lpar,'m'))
    snpsgrd.DSPAR.BASISNAME.putData('lpar from calc_xlength')
    snpsgrd.DSPAR.COMMENT.putData('Parallel distance from inner plate '+
                    'to cell center')

    # place holder for Coster's DSPOL parameter, Poloidal distance
    snpsgrd.DSPOL.putData(with_unit(lpol,'m'))
    snpsgrd.DSPOL.BASISNAME.putData('lpol from calc_xlength')
    snpsgrd.DSPOL.COMMENT.putData('Poloidal distance from inner plate '+
                    'to cell center')

    # place holder for Coster's DSRAD parameter, Radial distance
    snpsgrd.DSRAD.putData(with_unit(calc_ylength(),'m'))
    snpsgrd.DSRAD.BASISNAME.putData('lrad from calc_ylength')
    snpsgrd.DSRAD.COMMENT.putData('Radial distance from separatrix')

    # place holder for DSTARG parameters, distance along targets.
    # distance for target 1
    snpsgrd.DSTARG1.putData(with_unit(com.yylb[:,0],'m'))
    snpsgrd.DSTARG1.BASISNAME.putData('com.yylb[:,0]')
    snpsgrd.DSTARG1.COMMENT.putData('Distance along from ISP along IT')

    # distance for target 2 [for snull]
    snpsgrd.DSTARG2.putData(with_unit(com.yyrb[:,0],'m'))
    snpsgrd.DSTARG2.BASISNAME.putData('com.yyrb[:,0]')
    snpsgrd.DSTARG2.COMMENT.putData('Distance along from OSP along OT')
    
    # distance for target 2 for DN configuration
    if com.nxpt == 2: ### !!! How many come after if?
        snpsgrd.DSTARG2.putData(with_unit(com.yyrb[:,0],'m')) 
        snpsgrd.DSTARG2.BASISNAME.putData('com.yyrb[:,1]') 
        snpsgrd.DSTARG2.COMMENT.putData('Distance from 2nd ISP along IT') 

        # distance for target 3 [for DN]
        snpsgrd.DSTARG3.putData(with_unit(com.yylb[:,1],'m')) 
        snpsgrd.DSTARG3.BASISNAME.putData('com.yylb[:,1]') 
        snpsgrd.DSTARG3.COMMENT.putData('Distance from 2nd OSP along OT') 

        # distance for target 4 [for DN]
        snpsgrd.DSTARG4.putData(with_unit(com.yyrb[:,1],'m')) 
        snpsgrd.DSTARG4.BASISNAME.putData('com.yyrb[:,1]') 
        snpsgrd.DSTARG4.COMMENT.putData('Distance from OSP along OT') 

    # normalized poloidal flux at OMP
    snpsgrd.PSINRAD.putData((com.psi[bbb.ixmp,:,0]-com.simagx)/(com.sibdry-
                                com.simagx))
    snpsgrd.PSINRAD.BASISNAME.putData('(com.psi[bbb.ixmp,:,0]-com.simagx)/'+
                                    '(com.sibdry-com.simagx)')
    snpsgrd.PSINRAD.COMMENT.putData('Normalized poloidal flux radially at OMP')

    # place holder for Coster's POT parameter, Potential energy
    # AH - 19May21
    snpsgrd.POT.putData(with_unit(bbb.phi,'V'))
    snpsgrd.POT.BASISNAME.putData('bbb.phi')
    snpsgrd.POT.COMMENT.putData('Potential energy for each cell [V]')

    # place holder for Coster's POTI parameter, Ionization Potential

    # place holder for Coster's REGFLX parameter, x-directed flux region indices

    # place holder for Coster's REGFLY parameter, y-directed flux region indices

    # place holder for Coster's REGVOL parameter, volume region indices

    ''' INDICES FOR REGIONS PROJECTED ONTO PYTHON FULL (GCs INCLUDED) GRID '''
    snpsgrd.REGVOL.putData(make_regvol())
    snpsgrd.REGVOL.BASISNAME.putData('regvol as calculated by make_regvol')
    snpsgrd.REGVOL.COMMENT.putData( '1 for core, 2 for SOL abv xpt, 3 for '+
                                    'inner divertor, 4 for outer divertor')

    # Z-coordinate of cell centers, Z in machine coordinates
    snpsgrd.CZ.putData(with_unit(com.zm-com.zshift,'m'))
    snpsgrd.CZ.BASISNAME.putData('com.zm-com.zshift')
    snpsgrd.CZ.COMMENT.putData('Vertical coordinate of cell vertices, '+
            'machine coordinates. 3rd dimension order: CC, SW, SE, NW, NE')
    
    # R- and Z-coordinate of cell vertices, Z in machine coordinates
    snpsgrd.R.putData(with_unit(com.rm,'m'))
    snpsgrd.R.BASISNAME.putData('com.rm')
    snpsgrd.R.COMMENT.putData('Radius of cell vertices')

    snpsgrd.Z.putData(with_unit(com.zm-com.zshift,'m'))
    snpsgrd.Z.BASISNAME.putData('com.zm-com.zshift')
    snpsgrd.Z.COMMENT.putData('Vertical position of cell vertices, machine coordinates')
    
    # Vessel structure
    if com.nlim > 0:
        snpsgrd.VESSEL.putData(with_unit(array([com.xlim[:-1], com.ylim[:-1]
                        -com.zshift, com.xlim[1:], com.ylim[1:]-
                        com.zshift]).transpose(),'m'))
        snpsgrd.VESSEL.BASISNAME.putData('[com.xlim[:-1], com.ylim[:-1]-'+
                        'com.zshift, com.xlim[1:], com.ylim[1:]-com.zshift]')
        snpsgrd.VESSEL.COMMENT.putData('Data defining line segments of '+
                        'first wall')

    # Species charge charge
    snpsgrd.ZA.putData(make_fluidarray(bbb.ziin, zeros(bbb.natomic.shape)))
    snpsgrd.ZA.BASISNAME.putData('make_fluidarray(bbb.ziin, '+
                                'zeros(bbb.natomic.shape))')
    snpsgrd.ZA.COMMENT.putData('Charge of ion/neutral species')
    
    # Species nuclear charge
    snpsgrd.ZN.putData(make_fluidarray(bbb.znucl, bbb.natomic))
    snpsgrd.ZN.BASISNAME.putData('make_fluidarray(bbb.znucl, bbb.natomic)')
    snpsgrd.ZN.COMMENT.putData('Nuclear charge of ion/neutral species')

    return True

def store_snapshot_branch(tree):

    from uedge import com, bbb
    from numpy import array, zeros
    # -------------------------------------------------------------------------
    # Store SNAPSHOT branch

    snps = tree.SNAPSHOT

    # placeholder for Coster's alf parameter, thermo-electric coefficient

    # B fields: poloidal, radial, toroidal, total
    snps.B.putData(with_unit(array([com.bpol[:,:,0], com.br[:,:,0], 
                    com.bphi[:,:,0], com.b[:,:,0]]),'T'))
    snps.B.BASISNAME.putData('[com.bpol[:,:,0], com.br[:,:,0], '
                    +'com.btor[:,:,0], com.b[:,:,0]]')
    snps.B.COMMENT.putData('Magnetic field components at cell center: '+
                    '[poloidal, radial, toroidal, total]')
    
    # placeholder for Coster's D parameter, no comment

    # placeholder for Coster's DAB2 parameter, Atomic density

    # placeholder for Coster's DIB2 parameter, Test ion density

    # placeholder for Coster's DMB2, Molecular density

    # placeholder for Coster's DP parameter, Dpa

    # Poloidal electric current [GDP] - referenced to east [X] face
    snps.FCHX.putData(with_unit(bbb.fqx[:-1],'Amp'))
    snps.FCHX.BASISNAME.putData('bbb.fqx[:-1]')
    snps.FCHX.COMMENT.putData('Electric current across east face. '+
                'Note staggered grid: nx+1 omitted due to being a GC.')

    # Radial electric current - referenced to the north [Y] face
    snps.FCHY.putData(with_unit(bbb.fqy[:,:-1],'Amp'))
    snps.FCHY.BASISNAME.putData('bbb.fqy[:,:-1]')
    snps.FCHY.COMMENT.putData('Electric current across north face. '+
                'Note staggered grid: ny+1 omitted due to being a GC.')
    
    # Poloidal electron energy flux, east [X] face
    snps.FHEX.putData(with_unit(bbb.feex[:-1],'W'))
    snps.FHEX.BASISNAME.putData('bbb.feex[:-1]')
    snps.FHEX.COMMENT.putData('Electron energy flow across east face. '+
                'Note staggered grid: nx+1 omitted due to being a GC.')
    
    # Radial electron energy, north [Y] face
    snps.FHEY.putData(with_unit(bbb.feey[:,:-1],'W'))
    snps.FHEY.BASISNAME.putData('bbb.feey[:,:-1]')
    snps.FHEY.COMMENT.putData('Electron energy flow across north face. '+
                'Note staggered grid: ny+1 omitted due to being a GC.')

    # Total poloidal ion energy flux of each species, east [X] face
    snps.FHIX.putData(with_unit(bbb.feix[:-1],'W'))
    snps.FHIX.BASISNAME.putData('bbb.feix[:-1]')
    snps.FHIX.COMMENT.putData('Ion energy flow across east face. '+
                'Note staggered grid: nx+1 omitted due to being a GC.')
    
    # Total radial ion energy, north [Y] face
    snps.FHIY.putData(with_unit(bbb.feiy[:,:-1],'W'))
    snps.FHIY.BASISNAME.putData('bbb.feiy[:,:-1]')
    snps.FHIY.COMMENT.putData('Ion energy flow across north face. '+
                'Note staggered grid: ny+1 omitted due to being a GC.')

    # place holder for Coster's fhmx parameter, Poloidal kinetic energy flux
    # TODO: Implement

    # place holder for Coster's fhmy parameter, Radial kinetic energy flux
    # TODO: Implement

    # place holder for Coster's fhpx parameter, Poloidal potential energy flux
    # TODO: Implement

    # place holder for Coster's fhpy parameter, Radial  potential energy flux
    # TODO: Implement

    # place holder for Coster's fhtx parameter, Poloidal total energy flux
    # TODO: Implement

    # place holder for Coster's fhty parameter, Radial  total energy flux
    # TODO: Implement

    # Poloidal momentum current, east [X] face - resolved for all species 
    if bbb.isupgon[0] == 1: # Inertial neutrals
        snps.FMOX.putData(with_unit(bbb.fmix[:-1,:,::-1],'N'))
        snps.FMOX.BASISNAME.putData('bbb.fmix[:-1,:,::-1]')
        snps.FMOX.COMMENT.putData('Momentum across the east face. '+
                'Note staggered grid: nx+1 omitted due to being a GC. '+
                'NB: inertial atoms. 3rd dimension ordered [atom, ion]')
    else:
        snps.FMOX.putData(with_unit(bbb.fmix[:-1],'N'))
        snps.FMOX.BASISNAME.putData('bbb.fmix[:-1]')
        snps.FMOX.COMMENT.putData('Momentum across the east face. '+
                'Note staggered grid: nx+1 omitted due to being a GC. ')

    # Radial particle flux, north [Y] face  - resolved for all species 
    if bbb.isupgon[0] == 1: # Inertial neutrals
        snps.FMOY.putData(with_unit(bbb.fmiy[:,:-1,::-1],'N'))
        snps.FMOY.BASISNAME.putData('bbb.fmiy[:,:-1,::-1]')
        snps.FMOY.COMMENT.putData('Momentum across the north face. '+
                'Note staggered grid: nx+1 omitted due to being a GC. '+
                'NB: inertial atoms. 3rd dimension ordered [atom, ion]')
    else:
        snps.FMOY.putData(with_unit(bbb.fmiy[:,:-1],'N'))
        snps.FMOY.BASISNAME.putData('bbb.fmiy[:,:-1]')
        snps.FMOY.COMMENT.putData('Momentum across the north face. '+
                'Note staggered grid: nx+1 omitted due to being a GC. ')

    # Poloidal particle current, east [X] face - resolved for all species 
    snps.FNAX.putData(with_unit(make_fluidarray(bbb.fnix, bbb.fngx), '1/s'))
    snps.FNAX.BASISNAME.putData('fncx')
    snps.FNAX.COMMENT.putData('Particle current across east face.')

    # Radial particle flux, north [Y] face  - resolved for all species 
    snps.FNAY.putData(with_unit(make_fluidarray(bbb.fniy, bbb.fngy), '1/s'))
    snps.FNAY.BASISNAME.putData('fncy')
    snps.FNAY.COMMENT.putData('Particle current across north face.')

    # placeholder for Coster fnax_32 parameter, Poloidal particle flux [3/2 piece]

    # placeholder for Coster fnax_52 parameter, Poloidal particle flux [5/2 piece]

    # placeholder for Coster fnay_32 parameter, Radial particle flux [3/2 piece]

    # placeholder for Coster fnay_52 parameter, Radial particle flux [5/2 piece]

    # hx, length of cell
    snps.HX.putData(with_unit(1/com.gx,'m'))
    snps.HX.BASISNAME.putData('1/com.gx')
    snps.HX.COMMENT.putData('Poloidal length of primary cell')

    # hy, width of cell
    snps.HY.putData(with_unit(1/com.gy,'m'))
    snps.HY.BASISNAME.putData('1/com.gy')
    snps.HY.COMMENT.putData('Radial width of primary cell')

    # place holder for Coster's hy1 parameter, Corrected width of cell

    # place holder for Coster's bbb.kye parameter, bbb.kye
    # TODO: implement

    # place holder for Coster's bbb.kyi parameter, bbb.kyi
    # TODO: implement

    # place holder for Coster's kyi0 parameter, kyi0

    # Neutral/ion density
    snps.NA.putData(with_unit(make_fluidarray(bbb.ni, bbb.ng), '1/m**3'))
    snps.NA.BASISNAME.putData('make_fluidarray(bbb.ni, bbb.ng)')
    snps.NA.COMMENT.putData('Particle density in primary cell')

    # Electron density
    snps.NE.putData(with_unit(bbb.ne, '1/m**3'))
    snps.NE.BASISNAME.putData('bbb.ne')
    snps.NE.COMMENT.putData('Electron density in primary cells')
    
    # place holder for Coster's PEFA parameter, Poloidal atomic energy flux
    # TODO: Implement

    # place holder for Costers PEFM parameter, Poloidal molecular energy flux
    # TODO: Implement

    # place holder for Coster's PFLA parameter, Poloidal atomic flux
    # TODO: Implement

    # place holder for Coster's PFLM parameter, Poloidal molecular flux
    # TODO: Implement

    # Pressure
    snps.PR.putData(bbb.pr)
    snps.PR.BASISNAME.putData('bbb.pr')
    snps.PR.COMMENT.putData('Pressure in primary cells')

    # place holder for Coster's RCXHI parameter, CX ion energy neutral losses
    # TODO: Implement

    # place holder for Coster's RCXMO parameter, CX momentum neutral losses
    # TODO: Implement

    # place holder for Coster's RCXNA parameter, CX particle neutral losses
    # TODO: Implement

    # place holder for Coster's REFA parameter, Radial atomic energy flux
    # TODO: Implement

    # place holder for Costers REFM parameter, Radial molecular energy flux
    # TODO: Implement

    # place holder for Coster's RFLA parameter, Radial atomic flux
    # TODO: Implement

    # place holder for Coster's RFLM parameter, Radial molecular flux
    # TODO: Implement

    # Electron cooling rate
    # Total electron energy input = vsoree[,]/vol[,] [W/m3] hydrogenic loss
    # Total electron energy loss  = bbb.pwrze[,] [W/m3] impurity loss
    if (bbb.isimpon >= 5):
        snps.RQAHE.putData(with_unit(bbb.vsoree/com.vol - bbb.pwrze,'W/m**3'))
        snps.RQAHE.BASISNAME.putData('bbb.vsoree/com.vol - bbb.pwrze')
    else:
        snps.RQAHE.putData(bbb.vsoree/com.vol)
        snps.RQAHE.BASISNAME.putData('bbb.vsoree/com.vol')
    snps.RQAHE.COMMENT.putData('Power source into electrons in primary cell')

    # place holder for Coster's RQBRM parameter, Bremsstrahlung radiation api.rate
    # TODO: Implement

    # place holder for Coster's RQRAD parameter, Line radiation api.rate
    # TODO: Implement

    # place holder for Coster's RRAHI parameter, Recombination ion energy losses
    # TODO: Implement

    # place holder for Costers RRAMO parameter, Recombination momentum losses
    # TODO: Implement

    # place holder for Coster's RRANA parameter, Recombination particle losses
    # TODO: Implement

    # place holder for Coster's RSAHI parameter, Ionization ion energy losses
    # TODO: Implement

    # place holder for Coster's RSAMO parameter, Ionization momentum losses
    # TODO: Implement

    # place holder for Coster's RSANA parameter, Ionization particle losses
    # TODO: Implement

    # TODO: Implement additional molecular sinks/sources?

    # place holder for Coster's SIG parameter, anomalous conductivity

    # Poloidal cell face area
    snps.SX.putData(with_unit(com.sx[:-1],'m**2'))
    snps.SX.BASISNAME.putData('com.sx[:-1]')
    snps.SX.COMMENT.putData('Primary cell east face area.')

    # Radial cell face area
    snps.SY.putData(with_unit(com.sy[:,:-1],'m**2'))
    snps.SY.BASISNAME.putData('com.sy[:,:-1]')
    snps.SY.COMMENT.putData('Primary cell north face area.')

    # place holder for Coster's TAB2 parameter, Neutral atom temperature
    # TODO: Implement

    # Electron temperature
    snps.TE.putData(with_unit(bbb.te/bbb.ev,'eV'))
    snps.TE.BASISNAME.putData('bbb.te/bbb.ev')
    snps.TE.COMMENT.putData('Electron temperature in primary cell')

    # place holder for Coster's TEXTAN parameter, atom species

    # place holder for Coster's TEXTCOMP parameter, Components

    # place holder for Coster's TEXTIN parameter, Test ion species

    # place holder for Coster's TEXTMN parameter, Molecular species


    snps.TEXTPL.putData(str(make_fluidarray(None, None, label=True))[1:-1])
    snps.TEXTPL.BASISNAME.putData('make_fluidarray(None, None, label=True)')
    snps.TEXTPL.COMMENT.putData('Labels for plasma fluid species. '+
                        'Same as writing order.')

    # Ion temperature [UEDGE: all ions at same temperature]
    snps.TI.putData(with_unit(bbb.ti/bbb.ev,'eV'))
    snps.TI.BASISNAME.putData('bbb.ti/bbb.ev')
    snps.TI.COMMENT.putData('Ion temperature in primary cell')

    # place holder for Coster's TIB2 parameter, Test ion temperature

    # place holder for Coster's TMB2 parameter, Neutral molecule temperature

    # [Neutral]/Ion parallel velocity
    # TODO: Transform poloidal neutral velocity to parallel velocity?
    snps.UA.putData(with_unit(make_fluidarray(bbb.upi, bbb.uug),'m/s'))
    snps.UA.BASISNAME.putData('make_fluidarray(bbb.upi, bbb.uug)')
    snps.UA.COMMENT.putData('Parallel velocity (poloidal for neutral '+
                        'species) in primary cell')
    
     # place holder for Coster's VISC parameter, Viscosity
    # TODO: Implement

    # place holder for Coster's VLAX parameter, Poloidal pinch velocity

    # place holder for Coster's VLAY parameter, Radial pinch velocity

    # volume
    snps.VOL.putData(with_unit(com.vol,'m**3'))
    snps.VOL.BASISNAME.putData('com.vol')
    snps.VOL.COMMENT.putData('Volume of primary cells')

    return True


def store_ident_branch(tree):
    from datetime import datetime
    from os import getcwd
    from getpass import getuser
    from socket import gethostbyname, gethostname
    from uedge import bbb, com

    ident = tree.IDENT

    # place holder for Coster's parameter B2FGMTRYID, md5sum hash of b2fgmtry

    # place holder for Coster's parameter B2FPLAMSAID, md5sum hash of b2fplasma

    # place holder for Coster's parameter B2FSTATEID, md5sum hash of b2fstate

    # place holder for Coster's parameter BWFSTATIID, md5sum hash of b2stati

    # Date written to database
    ident.DATE.putData(datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
    ident.DATE.COMMENT.putData('Date and time when information written to MDSplus')

    # Directory in which the run was stored [GDP]
    ident.DIRECTORY.putData(getcwd())
    ident.DIRECTORY.COMMENT.putData('Directory where UEDGE case is run')

    # TODO: no "machine" parameter passed globally by Python: 
    # how should we account for this in the future?
    ident.EXP.putData('n/a')
    ident.EXP.COMMENT.putData('Experiment name not specified')


    # Geometry
    ident.GEOMETRY.putData(com.geometry[0].decode('UTF-8').strip())
    ident.GEOMETRY.BASISNAME.putData('com.geometry')
    ident.GEOMETRY.COMMENT.putData('Mnemonic for geometry')

    # Host identification
    ident.HOST.putData('Hostname: {}, host: {}'.format(gethostname(),
                        gethostbyname(gethostname())))
    ident.HOST.putData('Host running on when written to MDS+')

    # place holder for Coster's parameter MAIN, Label in b2fstate derived from b2mn.dat

    # Number of UEDGE fluid species
    ident.NS.putData(com.ngsp + com.nisp - 1*(bbb.isupgon[0]!=0))
    ident.NS.BASISNAME.putData('com.ngsp + com.nisp - 1*(bbb.isupgon[0]!=0)')
    ident.NS.COMMENT.putData('Number of fluid species')

    # Grid size in poloidal direction, including guard cells
    ident.NX.putData(com.nx+2)
    ident.NX.BASISNAME.putData('com.nx+2')
    ident.NX.COMMENT.putData('Number of poloidal cells, including guard cells')

    # Grid size in radial direction, including guard cells
    ident.NY.putData(com.ny+2)
    ident.NY.BASISNAME.putData('com.ny+2')
    ident.NY.COMMENT.putData('Number of radial cells, including guard cells')

    # place holder for Coster's parameter OBJECTCODE

    # place holder for Coster's parameter PHYSICS

    # Problem name
    ident.PROBNAME.putData(bbb.label[0].decode('UTF-8').strip())
    ident.PROBNAME.BASISNAME.putData('bbb.label')
    ident.PROBNAME.COMMENT.putData('Problem label')

    # Experiment shot number
    ident.SHOT.putData(com.eshot)
    ident.SHOT.BASISNAME.putData('com.eshot')
    ident.SHOT.COMMENT.putData('Experiment shot number')

    # List of plasma species
    ident.SPECIES.putData(str(make_fluidarray(None, None, label=True))[1:-1])
    ident.SPECIES.BASISNAME.putData('make_fluidarray(None, None, label=True)')
    ident.SPECIES.COMMENT.putData('List of strings for species handles. '+
                                'Order same as for shared arrays.')

    # Experiment shot time
    ident.TIME.putData(with_unit(com.etime*1e-3,'s'))
    ident.TIME.BASISNAME.putData('com.etime*1e-3')
    ident.TIME.COMMENT.putData('Experiment shot time (from EFIT equilibrium)')

    # place holder for Coster's parameter UEDGETOP

    # Store the current UEDGE version
    ident.UEDGEVERSION.putData(bbb.uedge_ver[0].decode('UTF-8').strip())
    ident.UEDGEVERSION.BASISNAME.putData(bbb.uedge_ver)
    ident.UEDGEVERSION.COMMENT.putData('UEDGE version number')

      # Store the user running the script
    ident.USER.putData(getuser())
    ident.USER.COMMENT.putData('User running the MDS+ write script')

    # Version number of this routine
    global version
    ident.VERSION.putData(version)
    ident.VERSION.COMMENT.putData('Version of the UEDGE MDS+ writing script')

    # Place holder for Coster's parameter CPU, the CPU running on

    return True

def store_ident_mpsep(tree, MPloc):
    ''' Writes inner/outer midplane profiles to MDS+'''
    from uedge import bbb, com
    from numpy import zeros

    if MPloc == 'IMP':   # Inner midplane profiles
        mp = tree.IDENT.IMPSEP
        row = find_iximp()
    elif MPloc == 'OMP': # Outer midplane profiles
        mp = tree.IDENT.OMPSEP
        row = bbb.ixmp
    else: 
        print('Unrecognized MPloc! Use MPloc == "IMP" or "OMP". Aborting.')
        return None


    # Inner midplane separatrix R
    mp.CR.putData(with_unit(0.5*sum(com.rm[row,com.iysptrx,3:]),'m'))
    mp.CR.BASISNAME.putData('0.5*sum(com.rm[row,com.iysptrx,3:])')
    mp.CR.COMMENT.putData('Separatrix radius at {}'.format(MPloc))

    # Inner midplane separatrix Z
    mp.CZ.putData(with_unit(0.5*sum(com.zm[row,com.iysptrx,3:]),'m'))
    mp.CZ.BASISNAME.putData('0.5*sum(com.zm[row,com.iysptrx,3:])')
    mp.CZ.COMMENT.putData('Separatrix vertical position at {}'.format(MPloc))

    # TODO: verify the coefficients for isbohmcalc=0!
    # Inner midplane separatrix diffusion coefficient 
    mp.D.putData(with_unit(make_fluidarray(bbb.dif_use, zeros(
            (bbb.ne.shape[0], bbb.ne.shape[1], com.ngsp)))[row,:],'m**2/s'))
    mp.D.BASISNAME.putData('make_fluidarray(bbb.dif_use, zeros((bbb.ne.'+
            'shape[0], bbb.ne.shape[1], com.ngsp)))[row,:]')
    mp.D.COMMENT.putData('{} radial diffusion coefficient profile'.format(
            MPloc))

    # Inner midplane separatrix electron bbb.diffusivity # base 0,   (0:nx+1,0:ny+1)
    mp.KYE.putData(with_unit(bbb.kye,'m**2/s'))
    mp.KYE.BASISNAME.putData('bbb.kye')
    mp.KYE.COMMENT.putData(MPloc+' radial electron heat diffusivity '+
            'radial profile')

    # Inner midplane separatix ion bbb.diffusivity for ns=1 # base 0,   (0:nx+1,0:ny+1)
    mp.KYI.putData(with_unit(bbb.kyi,'m**2/s'))
    mp.KYI.BASISNAME.putData('bbb.kyi')
    mp.KYI.COMMENT.putData(MPloc+' radial plasnma ion heat diffusivity '+
            'radial profile')

     # Placehholder, Coster's kyi0 inner midplane separatrix ion/atom diffusivity # base 0,   (0:nx+1,0:ny+1)

    # Inner midplane separatrix bbb.ne # base 0,   (0:nx+1,0:ny+1)
    mp.NE.putData(with_unit(bbb.ne[row,:],'1/m**3'))
    mp.NE.BASISNAME.putData('bbb.ne[row,:]')
    mp.NE.COMMENT.putData('Electron density profile at {} separatrix'.format(
            MPloc))

    # Inner midplane separatrix Te [eV]
    mp.TE.putData(with_unit(bbb.te[row,:]/bbb.ev,'eV'))
    mp.TE.BASISNAME.putData('bbb.te[row,:]/bbb.ev')
    mp.TE.COMMENT.putData('Electron temperature profile at {}'.format(MPloc)+
                    ' separatrix')

    # Inner midplane separatrix Ti [eV]
    mp.TI.putData(with_unit(bbb.ti[row,:]/bbb.ev,'eV'))
    mp.TI.BASISNAME.putData('bbb.ti[row,:]/bbb.ev')
    mp.TI.COMMENT.putData('Ion temperature profile at {}'.format(MPloc)+
                    ' separatrix')

    return True

def store_ident_sep(tree):
    from uedge import bbb, com
    from numpy import sum, ones

    sep = tree.IDENT.SEP

    # Core-SOL electron energy flow [W]
    sep.FHE.putData(with_unit(sum(bbb.feey[com.ixpt1[0]+1:com.ixpt2[0]+1, com.iysptrx]),'W'))
    sep.FHE.BASISNAME.putData('sum(bbb.feey[com.ixpt1[0]+1:com.ixpt2[0]+1, com.iysptrx])')
    sep.FHE.COMMENT.putData('Electron energy flow across the separatrix')

    # Core-SOL ion energy flow [W]
    sep.FHI.putData(with_unit(sum(bbb.feiy[com.ixpt1[0]+1:com.ixpt2[0]+1, com.iysptrx]),'W'))
    sep.FHI.BASISNAME.putData('sum(bbb.feiy[com.ixpt1[0]+1:com.ixpt2[0]+1, com.iysptrx])')
    sep.FHI.COMMENT.putData('Ion energy flow across the separatrix')

    # Core-SOL electron flow [W] [per GDP]
    mask = ones(bbb.fniy.shape)
    mask[:,:,1] = 0
    sep.FNE.putData(with_unit(sum(
            make_fluidarray(bbb.fniy*mask, 0*bbb.fngy)[
            com.ixpt1[0]+1:com.ixpt2[0]+1,com.iysptrx,:]), '1/s'))
    sep.FNE.BASISNAME.putData('sum(make_fluidarray(bbb.fniy*mask, 0*bbb.fngy)'+
            '[com.ixpt1[0]+1:com.ixpt2[0]+1,com.iysptrx,:])')
    sep.FNE.COMMENT.putData('Electron flux across the separatrix')

    # Core-SOL ion flow [W]
    sep.FNI.putData(with_unit(sum(
            make_fluidarray(bbb.fniy, bbb.fngy)[com.ixpt1[0]+1:com.ixpt2[0]+1,
            com.iysptrx,:],axis=0), '1/s'))
    sep.FNI.BASISNAME.putData('sum(make_fluidarray(bbb.fniy, bbb.fngy)'+
            '[com.ixpt1[0]+1:com.ixpt2[0]+1,com.iysptrx,:], axis=0)')
    sep.FNI.COMMENT.putData('Ion flux across the separatrix')

    return True



def write_shot(verbose=False):
    ''' Writes a UEDGE simulation to the next available shot number '''
    # Create a new tree in default order
    outtree = new_tree('uedge', verbose=verbose) 
    if outtree is False:
        return False
    if not store_snapshot_dimensions(outtree):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for SNAPSHOT.DIMENSIONS!'.format(outtree.shot))
        return False
    if not store_snapshot_grid(outtree):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for SNAPSHOT.GRID!'.format(outtree.shot))
        return False
    if not store_snapshot_branch(outtree):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for SNAPSHOT!'.format(outtree.shot))
        return False
    if not store_ident_branch(outtree):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for IDENT!'.format(outtree.shot))
        return False
    if not store_ident_mpsep(outtree, 'IMP'):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for IDENT.IMPSEP!'.format(outtree.shot))
        return False
    if not store_ident_mpsep(outtree, 'OMP'):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for IDENT.OMPSEP!'.format(outtree.shot))
        return False
    if not store_ident_sep(outtree):
        if verbose:
            print('ERROR')
            print('Data write to shot {} failed for IDENT.SEP!'.format(outtree.shot))
        return False
    if verbose:
        print('Data successfully written to shot {}'.format(outtree.shot))
    outtree.write()
    outtree.close()
    return outtree.shot
