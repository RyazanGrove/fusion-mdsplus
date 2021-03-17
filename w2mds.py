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
#
#
from uedge import *
from MDSplus import tree
import MDSplus.mdsarray as mdsarr
import numpy as np
import sys


yes=1
no=0


    
    
outtree = tree.Tree('uedge')
shot = outtree.incrementCurrent()
outtree.close()
# MG: force specific number, temporary fix since shot number was incremented
# even though tree were previously deleted
# Recommend using routine REWRITE_UEDGE2MDS!
# shot=999
try:
   outtree = tree.Tree('uedge',shot,'EDIT')
   print("Current shot is",shot,", already exists. Aborting.")
   outtree.close()
   sys.exit()
except:
   pass

outtree = tree.Tree('uedge')
outtree.createPulse(shot)
outtree = tree.Tree('uedge',shot,'EDIT')

def mdsput(*args):
    global outtree
    outtree.getNode(args[0]).putData(outtree.tdiCompile(*args[1:]))

# -------------------------------------------------------------------------
# store SNAPSHOT.DIMENSIONS                                               
snapshot = outtree.getNode('\\top.snapshot')
outtree.setDefault(snapshot)

# Index of the inner midplane
iximp=int((com.ixpt1 + 1 + grd.ixtop)/2)
test=com.zm[iximp-4:iximp+4,com.iysptrx,0]-com.zmagx 

for itest in np.arange(iximp-4,iximp+4):
   if abs(com.zm[itest,com.iysptrx,0]-com.zmagx) ==  min(abs(test)): iximp=itest 

# Write UEDGE variables and derived quantities to MDSplus

mdsput(".dimensions:imp","data($)",iximp)
mdsput(".dimensions:imp:basisname","data($)","From FIND_IXIMP: ~(ixpt1+1+ixptop]/2")
mdsput(".dimensions:imp:comment","data($)","poloidal index of IMP")

# Number of atomic species
natm=int(com.ngsp)
mdsput(".dimensions:natm","data($)",natm) 
mdsput(".dimensions:natm:basisname","data($)","com.ngsp")
mdsput(".dimensions:natm:comment","data($)","number of neutral species")

# place holder for Coster's NION parameter, number of test ion species

# place holder for Coster's NMOL parameter, number of molecular species

# Number of fluid species: UEDGE treats D and Imp atoms as fluid species! 
if bbb.isupgon[0] == 0:
    ns=int(com.nisp+com.ngsp)              # diffusive neutrals
    mdsput(".dimensions:ns:basisname","data($)","ns=com.nisp+com.ngsp")
else:
    ns=int(com.nisp+com.ngsp-1)            # inertial neutrals
    mdsput(".dimensions:ns:basisname","data($)","ns=com.nisp+com.ngsp-1")

mdsput(".dimensions:ns","data($)",ns) 
mdsput(".dimensions:ns:comment","data($)","Number of fluid species")

# Number of cells in parallel [poloidal] directions, including guard cells
mdsput(".dimensions:nx","data($)",com.nx+2)
mdsput(".dimensions:nx:basisname","data($)","com.nx+2")
mdsput(".dimensions:nx:comment","data($)","Number of cells in poloidal direction")

# Number of cells in radial directions, including guard cells
mdsput(".dimensions:ny","data($)",com.ny+2)
mdsput(".dimensions:ny:basisname","data($)","com.ny+2")
mdsput(".dimensions:ny:comment","data($)","Number of cells in radial direction")

# Index of the outer midplane
mdsput(".dimensions:omp","data($)",bbb.ixmp)
mdsput(".dimensions:omp:basisname","data($)","bbb.ixmp")
mdsput(".dimensions:omp:comment","data($)","poloidal index of OMP")

# Index of the separatrix
mdsput(".dimensions:sep:basisname","data($)","com.iysptrx")
mdsput(".dimensions:sep","data($)",com.iysptrx)
mdsput(".dimensions:sep:comment","data($)","flx.y index of separatrix")

# Index of the target 1 
mdsput(".dimensions:targ1","data($)",com.ixlb[0])
mdsput(".dimensions:targ1:basisname","data($)","com.ixlb[0]")
mdsput(".dimensions:targ1:comment","data($)","index of target 1")

# Index of the target 2 [for snull]
mdsput(".dimensions:targ2","data($)",com.ixrb[0])
mdsput(".dimensions:targ2:basisname","data($)","com.ixrb[0]")
mdsput(".dimensions:targ2:comment","data($)","index of target 4")

# Index of the target 2 [for DN]
if com.nxpt == 2:
   mdsput(".dimensions:targ2","data($)",com.ixrb[0])
   mdsput(".dimensions:targ2:basisname","data($)","com.ixrb[0]")
   mdsput(".dimensions:targ2:comment","data($)","index of target 2")

   # Index of the target 3
   mdsput(".dimensions:targ3","data($)",com.ixlb[1])
   mdsput(".dimensions:targ3:basisname","data($)","com.ixlb[1]")
   mdsput(".dimensions:targ3:comment","data($)","index of target 3")
   
   # Index of the target 4 [if DN]
   mdsput(".dimensions:targ4:basisname","data($)","com.ixrb[1]")
   mdsput(".dimensions:targ4","data($)",com.ixrb[1])
   mdsput(".dimensions:targ4:comment","data($)","index of target 4")

# end of SNAPSHOT.DIMENSIONS
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# store SNAPSHOT.GRID

# Atom/ion mass [AMU]: deuterium neutral, deuterium ion, impurity neutral, impurity ions,
am = np.zeros(ns)
for ii in np.range(1,com.nhgsp+1):
   am[2*(ii-1)]=bbb.mg[ii-1]/bbb.mp
   am[2*(ii-1)+1]=bbb.minu[ii-1]

if bbb.isimpon >= 5 : # multi species impurity
   nsm1=int(2*com.nhgsp)
   for igsp in np.range(com.nhgsp+1,com.ngsp+2):
      jz=int(igsp-com.nhgsp)
      am[nsm1+jz-1]=bbb.mg[igsp-1]/bbb.mp
      for ifld in range(1,com.nzsp[jz-1]+1):
         am[nsm1+jz+ifld-1]=bbb.minu[nsm1+ifld-1]
      nsm1=nsm1+com.nzsp[jz-1]

mdsput(".grid:am","data($)",am)
mdsput(".grid:am:basisname","data($)","see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".grid:am:comment","data($)","ion/neutral mass [amu]")

# Generate UEDGE variables for rightix, leftix, etc.
rightix = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
leftix = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
topix = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
bottomix = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
leftiy = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
rightiy = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
topiy = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)
bottomiy = np.zeros((com.nx+2,com.ny+2),dtype=np.int32)

for ix in np.arange(0, com.nx+2):
   for iy in np.arange(0, com.ny+2):
      leftix[ix,iy]=bbb.idxm1
      rightix[ix,iy]=bbb.idxp1
      bottomix[ix,iy]=max(0,ix+1)
      topix[ix,iy]=min(com.nx+1,ix+1)

      topiy[ix,iy]=bbb.idyp1
      bottomiy[ix,iy]=bbb.idym1
      leftiy[ix,iy]=max(0,iy+1)
      rightiy[ix,iy]=min(com.ny+1,iy+1)


mdsput(".grid:rightix:basisname","data($)","bbb.idxp1")
mdsput(".grid:rightix","data($)",rightix)

mdsput(".grid:leftix:basisname","data($)","bbb.idxm1")
mdsput(".grid:leftix","data($)",leftix)

mdsput(".grid:topix:basisname","data($)","min[com.nx+1,bbb.ix+1")
mdsput(".grid:topix","data($)",topix)

mdsput(".grid:bottomix:basisname","data($)","max[0,bbb.ix+1")
mdsput(".grid:bottomix","data($)",bottomix)

mdsput(".grid:topiy:basisname","data($)","bbb.idyp1")
mdsput(".grid:topiy","data($)",topiy)

mdsput(".grid:bottomiy:basisname","data($)","bbb.idym1")
mdsput(".grid:bottomiy","data($)",bottomiy)

mdsput(".grid:leftiy:basisname","data($)","max[0,bbb.ix+1]")
mdsput(".grid:leftiy","data($)",leftiy)

mdsput(".grid:rightiy:basisname","data($)","max[com.ny+1,bbb.ix+1")
mdsput(".grid:rightiy","data($)",rightiy)

# R- coordinate of cell centers, Z in machine coordinates
trm=com.rm[:,:,0] # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr","data($)",trm)
mdsput(".grid:cr:basisname","data($)","com.rm[,,0]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr:comment","data($)","Radial coordinate of cell center [grd.m]")

# normalized poloidal flux of each cell
if not 'psin' in locals():
    psin=(com.psi[0:com.nx+2,0:com.ny+2,0]-com.simagx)/(com.sibdry-com.simagx) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:psin","data($)",psin)
mdsput(".grid:psin:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".grid:psin:comment","data($)","Normalized poloidal flux in cells")



#
# checked to here - Bill Meyer
#
# R- and Z-coordinate of cell east [X] face, Z in machine coordinates
trm=0.5*(com.rm[0:com.nx+1,:,2]+com.rm[0:com.nx+1,:,4]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr_x","data($)",trm)
mdsput(".grid:cr_x:basisname","data($)","0.5*[com.rm[0:com.nx,,2]+com.rm[0:com.nx,,4]]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr_x:comment","data($)","radial coordinate of east face [grd.m]")

trm=0.5*(com.zm[0:com.nx+1,:,2]+com.zm[0:com.nx+1,:,4]-com.zshift) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cz_x","data($)",trm)
mdsput(".grid:cz_x:basisname","data($)","0.5*[com.zm[0:com.nx,,2]+com.zm[0:com.nx,,4]]-com.zshift") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cz_x:comment","data($)","vertical coordinate of east face, machine coordinates [grd.m]")

# R- and Z-coordinate of cell north [Y] face, Z in machine coordinates
trm=0.5*(com.rm[:,0:com.ny+1,3]+com.rm[:,0:com.ny+1,4]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr_y","data($)",trm)
mdsput(".grid:cr_y:basisname","data($)","0.5*[com.rm[,0:com.ny,3]+com.rm[,0:com.ny,4]]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cr_y:comment","data($)","radial coordinate of north face [grd.m]")
trm=0.5*(com.zm[:,0:com.ny+1,3]+com.zm[:,0:com.ny+1,4])-com.zshift # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cz_y","data($)",trm)
mdsput(".grid:cz_y:basisname","data($)","0.5*[com.zm[,0:com.ny,3]+com.zm[,0:com.ny,4]]-com.zshift") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cz_y:comment","data($)","Vertical coordinate of north face, machine coordinates, [grd.m]")

# place holder for Coster's DSPAR parameter, Parallel distance
if not 'iscalc_length' in locals(): iscalc_length=no
if iscalc_length == no:  

   lpol = np.zeros((com.nx+2,com.ny+2))
   lparal = np.zeros((com.nx+2,com.ny+2))
   lpolf = np.zeros((com.nx+2,com.ny+2))
   lparalf = np.zeros((com.nx+2,com.ny+2))
   for iy in np.arange(com.ny+2):
      lpolf[0,iy] = 1./com.gx[0,iy]
      lpol[0,iy] = 0.5/com.gx[0,iy]
      lparal[0,iy] = 0.5/com.gx[0,iy]/com.rr[0,iy]
      lparalf[0,iy] = 1.0/com.gx[0,iy]/com.rr[0,iy]
      for ix in np.arange(1,com.nx+2):
         lpolf[ix,iy] = 1.0 ### !!! Dummy value added

   mdsput(".grid:dspar","data($)",lparal)
   mdsput(".grid:dspar:basisname","data($)","lparal from calc_lengths")
   mdsput(".grid:dspar:comment","data($)","parallel distance from inner plate [grd.m]")

   # place holder for Coster's DSPOL parameter, Poloidal distance
   mdsput(".grid:dspol","data($)",lpol)
   mdsput(".grid:dspol:basisname","data($)","lpol from calc_lengths")
   mdsput(".grid:dspol:comment","data($)","poloidal distance from inner plate [grd.m]")
   
   # place holder for Coster's DSRAD parameter, Radial distance
#   if [.not. exists["iscalc_radius"]] integer iscalc_radius=no ### !!! Where exists function comes from?
#   if [iscalc_radius .eq. no] read calc_radius ### !!! How to read calc_radius? 
   mdsput(".grid:dsrad","data($)",lrad)
   mdsput(".grid:dsrad:basisname","data($)","lrad from calc_radius")
   mdsput(".grid:dsrad:comment","data($)","radial distance from separatrix [grd.m]")

   # place holder for DSTARG parameters, distance along targets.
   # distance for target 1
   mdsput(".grid:dstarg1","data($)",com.yylb[1]) # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg1.basisname","data($)","com.yylb[1]") # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg1.comment","data($)","distance from ISP [grd.m]")

   # distance for target 2 [for snull]
   mdsput(".grid:dstarg2","data($)",com.yyrb[1]) # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg2.basisname","data($)","com.yyrb[1]") # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg2.comment","data($)","distance from OSP [grd.m]")

   # distance for target 2 for DN configuration
   if com.nxpt == 2: ### !!! How many come after if?
       mdsput(".grid:dstarg2","data($)",com.yyrb[1]) # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg2.basisname","data($)","com.yyrb[1]") # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg2.comment","data($)","distance from 2nd ISP [grd.m]")
   
   # distance for target 3 [for DN]
   mdsput(".grid:dstarg3","data($)",com.yylb[2]) # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg3.basisname","data($)","com.yylb[2]") # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg3.comment","data($)","distance from 2nd OSP [grd.m]")
   
   # distance for target 4 [for DN]
   mdsput(".grid:dstarg4","data($)",com.yyrb[2]) # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg4.basisname","data($)","com.yyrb[2]") # base 0,   (0:ny+1,1:nxpt)
   mdsput(".grid:dstarg4.comment","data($)","distance from OSP [grd.m]")

# normalized poloidal flux at OMP
mdsput(".grid:psinrad","data($)",psin[bbb.ixmp,])
mdsput(".grid:psinrad:basisname","data($)","psin[bbb.ixmp,]")
mdsput(".grid:psinrad:comment","data($)","normalized poloidal flux radially at OMP")

# place holder for Coster's POT parameter, Potential energy

# place holder for Coster's POTI parameter, Ionization Potential

# place holder for Coster's REGFLX parameter, flx.x-directed flux region indices

# place holder for Coster's REGFLY parameter, flx.y-directed flux region indices

# place holder for Coster's REGVOL parameter, volume region indices
core=range(com.ixpt1+1,com.ixpt2)  ### !!! range core=com.ixpt1+1:com.ixpt2
### !!! integer regvol[0:com.nx+1,0:com.ny+1]
regvol[core,0:com.iysptrx]=1
regvol[core,com.iysptrx+1:com.ny+1]=2
regvol[0:com.ixpt1,0:com.ny+1]=3
regvol[com.ixpt2+1:com.nx+1,0:com.ny+1]=4
mdsput(".grid:regvol","data($)",regvol)
mdsput(".grid:regvol:basisname","data($)","N/A")
mdsput(".grid:regvol:comment","data($)","1 for core, 2 for SOL abv xpt, 3 for inner divertor, 4 for outer divertor")

# Z-coordinate of cell centers, Z in machine coordinates
mdsput(".grid:cz:basisname","data($)","com.zm[,,0]-com.zshift") # base 0,   (0:nxm+1,0:nym+1,0:4)
trm[0:com.nx+1,0:com.ny+1]=com.zm[:,:,0]-com.zshift # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:cz","data($)",trm)
mdsput(".grid:cz:comment","data($)","Vertical coordinate of cell center, machine coordinates [grd.m]")

# R- and Z-coordinate of cell vertices, Z in machine coordinates
mdsput(".grid:r","data($)",com.rm[:,:,1:4]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:r:basisname","data($)","com.rm[,,1:4]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:r:comment","data($)","radius of cell vertices [grd.m]")
mdsput(".grid:z","data($)",com.zm[:,:,1:4]-com.zshift) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:z:basisname","data($)","com.zm[,,1:4]-com.zshift") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".grid:z:comment","data($)","Z of cell vertices, machine coordinates [grd.m]")

# Vessel structure
# test on com.xlim added for api.one of Rognlien's benchmark cases
if com.nlim > 0:
    mdsput(".grid:vessel","data($)",transpose[[com.xlim[1:shape[com.xlim]-1],com.ylim[1:shape[com.ylim]-1]-com.zshift,com.xlim[2:shape[com.xlim]],com.ylim[2:shape[com.ylim]]-com.zshift]])
endif
mdsput(".grid:vessel:basisname","data($)","com.xlim[0], com.ylim[0]-com.zshift, com.xlim[1], com.ylim[1]-com.zshift")
mdsput(".grid:vessel:comment","data($)","Data defining line segments of first wall [grd.m]")

# Atom charge
real za[ns]
integer bbb.igsp,ifld,ii
do ii=1,com.nhgsp
za[2*[ii-1]+1]=0.
za[2*[ii-1]+2]=api.bbb.zi[ii]
enddo

if [bbb.isimpon .ge. 5] then  # multi species impurity
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
za[nsm1+jz]=0.
do ifld=1,com.nzsp[jz]
za[nsm1+jz+ifld]=api.bbb.zi[nsm1+ifld]
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(".grid:za","data($)",za)
mdsput(".grid:za:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".grid:za:comment","data($)","Charge of ion/neutral species")

# Nuclear charge
real zn[ns]
integer bbb.igsp,ifld,ii
do ii=1,com.nhgsp
zn[2*[ii-1]+1]=1.
zn[2*[ii-1]+2]=1.
enddo

if [bbb.isimpon .ge. 5] then  # multi species impurity
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
zn[nsm1+jz]=bbb.znucl[nsm1+jz]
do ifld=1,com.nzsp[jz]
zn[nsm1+jz+ifld]=bbb.znucl[nsm1+ifld]
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(".grid:zn","data($)",zn)
mdsput(".grid.zn:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".grid:zn:comment","data($)","Nuclear charge of ion/neutral species")

# end SNAPSHOT.GRID
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# Store SNAPSHOT branch

# placeholder for Coster's alf parameter, thermo-electric coefficient

# B fields: poloidal, radial, toroidal, total
real bppol[0:com.nx+1,0:com.ny+1]=com.com.bpol[,,0] # base 0,   (0:nxm+1,0:nym+1,0:4)
real btor[0:com.nx+1,0:com.ny+1]=com.com.bphi[,,0] # base 0,   (0:nxm+1,0:nym+1,0:4)
real brad[0:com.nx+1,0:com.ny+1]=com.com.br[,,0] # base 0,   (0:nxm+1,0:nym+1,0:4)
real bbb.btot[0:com.nx+1,0:com.ny+1]=com.com.b[,,0] # base 0,   (0:nxm+1,0:nym+1,0:4) # base 0,   (0:nx+1,0:ny+1)
mdsput(":b","build_signal[build_with_units[$,""T""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",[bppol[0:com.nx+1,0:com.ny+1],brad[0:com.nx+1,0:com.ny+1],btor[0:com.nx+1,0:com.ny+1],bbb.btot[0:com.nx+1,0:com.ny+1]]]  # base 0,   (0:nxm+1,0:nym+1,0:4) # base 0,   (0:nx+1,0:ny+1)
mdsput(":b:basisname","data($)","[com.com.bpol,com.br,com.bphi,com.b]") # base 0,   (0:nxm+1,0:nym+1,0:4) # base 0,   (0:nxm+1,0:nym+1,0:4) # base 0,   (0:nxm+1,0:nym+1,0:4) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(":b:comment","data($)","magnetic field components [T]") # base 0,   (0:nxm+1,0:nym+1,0:4)

# placeholder for Coster's D parameter, no comment

# placeholder for Coster's DAB2 parameter, Atomic density

# placeholder for Coster's DIB2 parameter, Test ion density

# placeholder for Coster's DMB2, Molecular density

# placeholder for Coster's DP parameter, Dpa

# Poloidal electric current [GDP] - referenced to east [X] face
real fchx[0:com.nx,0:com.ny+1]=bbb.fqx[0:com.nx,0:com.ny+1] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fchx","build_signal[build_with_units[$,""Amp""],,\top.snapshot.grid:cr_x,\top.snapshot.grid:cz_x,\top.snapshot:textpl]",fchx)
mdsput(":fchx:basisname","data($)","bbb.fqx[0:com.nx,]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".fchx:comment","data($)","electric current across east face [Amp]")

# Radial electric current - referenced to the north [Y] face
real fchy[0:com.nx+1,0:com.ny]=bbb.fqy[0:com.ny+1,0:com.ny] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fchy","build_signal[build_with_units[$,""Amp""],,\top.snapshot.grid:cr_y,\top.snapshot.grid:cz_y,\top.snapshot:textpl]",fchy)
mdsput(":fchy:basisname","data($)","fqyy[,0:com.ny]")
mdsput(".fchy:comment","data($)","electric current across north face [Amp]")

# Poloidal electron energy flux, east [X] face
real fhex[0:com.nx,0:com.ny+1]=bbb.feex[0:com.nx,] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fhex","build_signal[build_with_units[$,""W""],,\top.snapshot.grid:cr_x,\top.snapshot.grid:cz_x]",fhex)
mdsput(":fhex:basisname","data($)","bbb.feex[0:com.nx,]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".fhex:comment","data($)","electron energy flow across east face [W]")

# Radial electron energy, north [Y] face
real fhey[0:com.nx+1,0:com.ny]=bbb.feey[,0:com.ny] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fhey","build_signal[build_with_units[$,""W""],,\top.snapshot.grid:cr_y,\top.snapshot.grid:cz_y]",fhey)
mdsput(":fhey:basisname","data($)","bbb.feey[,0:com.ny]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".fhey:comment","data($)","electron energy flow across north face [W]")

# Total poloidal ion energy flux of each species, east [X] face
real fhix[0:com.nx,0:com.ny+1]=bbb.feix[0:com.nx,] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fhix","build_signal[build_with_units[$,""W""],,\top.snapshot.grid:cr_x,\top.snapshot.grid:cz_x]",fhix)
mdsput(":fhix:basisname","data($)","bbb.feix[0:com.nx,]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".fhix:comment","data($)","Ion energy flow across east face [W]")

# Total radial ion energy, north [Y] face
real fhiy[0:com.nx+1,0:com.ny]=bbb.feiy[,0:com.ny] # base 0,   (0:nx+1,0:ny+1)
mdsput(":fhiy","build_signal[build_with_units[$,""W""],,\top.snapshot.grid:cr_y,\top.snapshot.grid:cz_y]",fhiy)
mdsput(":fhiy:basisname","data($)","bbb.feiy[,0:com.ny]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".fhiy:comment","data($)","Ion energy flow across north face [W]")

# place holder for Coster's fhmx parameter, Poloidal kinetic energy flux

# place holder for Coster's fhmy parameter, Radial kinetic energy flux

# place holder for Coster's fhpx parameter, Poloidal potential energy flux

# place holder for Coster's fhpy parameter, Radial  potential energy flux

# place holder for Coster's fhtx parameter, Poloidal total energy flux

# place holder for Coster's fhty parameter, Radial  total energy flux

# Poloidal momentum current, east [X] face - resolved for all species 
real fmox[0:com.nx,0:com.ny+1,2]
fmox[,,1]=0
if [bbb.isupgon[1] .eq. 1] fmox[,,1]=bbb.fmix[0:com.nx,,2] # base 0,   (0:nx+1,0:ny+1,1:nusp)
fmox[,,2]=bbb.fmix[0:com.nx,,1] # base 0,   (0:nx+1,0:ny+1,1:nusp)

mdsput(":fmox","build_signal[build_with_units[$,""Nwt""],,\top.snapshot.grid:cr_x,\top.snapshot.grid:cz_x,\top.snapshot:textpl[0:1]]",fmox)
mdsput(":fmox:basisname","data($)","bbb.fmix[0:com.nx,,]") # base 0,   (0:nx+1,0:ny+1,1:nusp)
mdsput(".fmox:comment","data($)","momentum across east face [Nwt]")

# Radial particle flux, north [Y] face  - resolved for all species 
real fmoy[0:com.nx+1,0:com.ny,2]
fmoy[,,1]=0.
if [bbb.isupgon[1] .eq. 1] fmoy[,,1]=bbb.fmiy[,0:com.ny,2] # base 0,   (0:nx+1,0:ny+1,1:nusp)
fmoy[,,2]=bbb.fmiy[,0:com.ny,1] # base 0,   (0:nx+1,0:ny+1,1:nusp)

mdsput(":fmoy","build_signal[build_with_units[$,""Nwt""],,\top.snapshot.grid:cr_y,\top.snapshot.grid:cz_y,\top.snapshot:textpl[0:1]]",fmoy)
mdsput(":fmoy:basisname","data($)","bbb.fmiy[,0:com.ny,]") # base 0,   (0:nx+1,0:ny+1,1:nusp)
mdsput(".fmoy:comment","data($)"," momentum across north face [Nwt]")

# Poloidal particle current, east [X] face - resolved for all species 
# don't use bbb.fnax for variable since already exists
real fncx[0:com.nx,0:com.ny+1,ns]
integer bbb.igsp,ifld,ii
# note this indexing does not com.work if there is more than api.one inertial neutral
do ii=1,com.nhgsp
fncx[,,2*[ii-1]+1]=bbb.fngx[0:com.nx,,ii] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
fncx[,,2*[ii-1]+2]=bbb.fnix[0:com.nx,,ii] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo

if [bbb.isimpon .ge. 5] then  # multi species impurities
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
fncx[,,nsm1+jz]=bbb.fngx[0:com.nx,,jz] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
do ifld=1,com.nzsp[jz]
fncx[,,nsm1+jz+ifld]=bbb.fnix[0:com.nx,,nsm1+ifld] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(":fnax","build_signal[build_with_units[$,""s-1""],,\top.snapshot.grid:cr_x,\top.snapshot.grid:cz_x,\top.snapshot:textpl]",fncx)
mdsput(":fnax:basisname","data($)","bbb.fngx[0:com.nx,,] and bbb.fnix[0:com.nx,,]") # base 0,   (0:nx+1,0:ny+1,1:nisp) # base 0,   (0:nx+1,0:ny+1,1:ngsp)
mdsput(":fnax:comment","data($)","particle current across east face [s^-1]")

# placeholder for Coster fnax_32 parameter, Poloidal particle flux [3/2 piece]

# placeholder for Coster fnax_52 parameter, Poloidal particle flux [5/2 piece]

# Radial particle flux, north [Y] face  - resolved for all species 
# don't use bbb.fnay for variable since it already exists
real fncy[0:com.nx+1,0:com.ny,ns]
integer bbb.igsp,ifld,ii
# note this indexing does not com.work if there is more than api.one inertial neutral
do ii=1,com.nhgsp
fncy[,,2*[ii-1]+1]=bbb.fngy[,0:com.ny,ii] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
fncy[,,2*[ii-1]+2]=bbb.fniy[,0:com.ny,ii] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo

if [bbb.isimpon .ge. 5] then  # multi species impurities
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
fncy[,,nsm1+jz]=bbb.fngy[,0:com.ny,jz] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
do ifld=1,com.nzsp[jz]
fncy[,,nsm1+jz+ifld]=bbb.fniy[,0:com.ny,nsm1+ifld] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(":fnay","build_signal[build_with_units[$,""s-1""],,\top.snapshot.grid:cr_y,\top.snapshot.grid:cz_y,\top.snapshot:textpl]",fncy)
mdsput(":fnay:basisname","data($)","bbb.fngy[,0:com.ny,] and bbb.fniy[,0:com.ny,]") # base 0,   (0:nx+1,0:ny+1,1:nisp) # base 0,   (0:nx+1,0:ny+1,1:ngsp)
mdsput(":fnay:comment","data($)","particle current across north face [s^-1]")

# placeholder for Coster fnay_32 parameter, Radial particle flux [3/2 piece]

# placeholder for Coster fnay_52 parameter, Radial particle flux [5/2 piece]

# hx, length of cell
real hx[0:com.nx+1,0:com.ny+1]=1/com.gx # base 0,   (0:nx+1,0:ny+1)
mdsput(":hx","build_signal[build_with_units[$,""grd.m""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",hx)
mdsput(":hx:basisname","data($)","1/com.gx") # base 0,   (0:nx+1,0:ny+1)
mdsput(".hx:comment","data($)","length of primary cells [grd.m]")

# hy, width of cell
real hy[0:com.nx+1,0:com.ny+1]=1/com.gy # base 0,   (0:nx+1,0:ny+1)
mdsput(":hy","build_signal[build_with_units[$,""grd.m""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",hy)
mdsput(":hy:basisname","data($)","1/com.gy") # base 0,   (0:nx+1,0:ny+1)
mdsput(".hy:comment","data($)","width of primary cells [grd.m]")

# place holder for Coster's hy1 parameter, Corrected width of cell

# place holder for Coster's bbb.kye parameter, bbb.kye

# place holder for Coster's bbb.kyi parameter, bbb.kyi

# place holder for Coster's kyi0 parameter, kyi0

# Neutral/ion density
real iondens[0:com.nx+1,0:com.ny+1,ns]

integer bbb.igsp,ifld,ii
# note this indexing does not com.work if there is more than api.one inertial neutral
do ii=1,com.nhgsp
iondens[,,2*[ii-1]+1]=bbb.ng[,,ii] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
iondens[,,2*[ii-1]+2]=bbb.ni[,,ii] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo

if [bbb.isimpon .ge. 5] then  # multi species impurities
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
iondens[,,nsm1+jz]=bbb.ng[,,bbb.igsp] # base 0,   (0:nx+1,0:ny+1,1:ngsp)
do ifld=1,com.nzsp[jz]
iondens[,,nsm1+jz+ifld]=bbb.ni[,,nsm1+ifld] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(":na","build_signal[build_with_units[$,""grd.m-3""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz,\top.snapshot:textpl]",iondens) # base 0,   (0:nx+1,0:ny+1)
mdsput(":na:basisname","data($)","bbb.ng[,,] and bbb.ni[,,]") # base 0,   (0:nx+1,0:ny+1,1:nisp) # base 0,   (0:nx+1,0:ny+1,1:ngsp) # base 0,   (0:nx+1,0:ny+1)
mdsput(":na:comment","data($)","particle density in primary cells [grd.m^-3]") # base 0,   (0:nx+1,0:ny+1)

# Electron density
mdsput(":ne","build_signal[build_with_units[$,""grd.m-3""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",bbb.ne) # base 0,   (0:nx+1,0:ny+1)
mdsput(":ne:basisname","data($)","bbb.ne[,]") # base 0,   (0:nx+1,0:ny+1)
mdsput(":ne:comment","data($)","electron density in primary cells [grd.m^-3]") # base 0,   (0:nx+1,0:ny+1)

# place holder for Coster's PEFA parameter, Poloidal atomic energy flux

# place holder for Costers PEFM parameter, Poloidal molecular energy flux

# place holder for Coster's PFLA parameter, Poloidal atomic flux

# place holder for Coster's PFLM parameter, Poloidal molecular flux

# Pressure
mdsput(":pr","build_signal[build_with_units[$,""J/m3""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",bbb.pr) # base 0,   (0:nx+1,0:ny+1)
mdsput(":pr:basisname","data($)","bbb.pr") # base 0,   (0:nx+1,0:ny+1)
mdsput(":pr:comment","data($)","Pressure in primary cells [J/m3]") # base 0,   (0:nx+1,0:ny+1)

# place holder for Coster's RCXHI parameter, CX ion energy neutral losses

# place holder for Coster's RCXMO parameter, CX momentum neutral losses

# place holder for Coster's RCXNA parameter, CX particle neutral losses

# place holder for Coster's REFA parameter, Radial atomic energy flux

# place holder for Costers REFM parameter, Radial molecular energy flux

# place holder for Coster's RFLA parameter, Radial atomic flux

# place holder for Coster's RFLM parameter, Radial molecular flux

# Electron cooling api.rate
# TDR: Total electron energy input = bbb.vsoree[,]/com.vol[,] [W/m3] hydrogenic loss # base 0,   (0:nx+1,0:ny+1) # base 0,   (0:nx+1,0:ny+1)
#      Total electron energy loss  = bbb.pwrze[,]         [W/m3] impurity loss # base 0,   (0:nx+1,0:ny+1)
if [bbb.isimpon .ge. 5] then
real rqahe[0:com.nx+1,0:com.ny+1]=-bbb.vsoree[,]/com.vol[,]+bbb.pwrze[,] # base 0,   (0:nx+1,0:ny+1) # base 0,   (0:nx+1,0:ny+1) # base 0,   (0:nx+1,0:ny+1)
else
real rqahe[0:com.nx+1,0:com.ny+1]=-bbb.vsoree[,]/com.vol[,] # base 0,   (0:nx+1,0:ny+1) # base 0,   (0:nx+1,0:ny+1)
endif

mdsput(":rqahe","build_signal[build_with_units[$,""W/m3""],,]",rqahe)
mdsput(":rqahe:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".rqahe:comment","data($)","Power source into electrons in primary cell [W/m3]")

# place holder for Coster's RQBRM parameter, Bremsstrahlung radiation api.rate

# place holder for Coster's RQRAD parameter, Line radiation api.rate

# place holder for Coster's RRAHI parameter, Recombination ion energy losses

# place holder for Costers RRAMO parameter, Recombination momentum losses

# place holder for Coster's RRANA parameter, Recombination particle losses

# place holder for Coster's RSAHI parameter, Ionization ion energy losses

# place holder for Coster's RSAMO parameter, Ionization momentum losses

# place holder for Coster's RSANA parameter, Ionization particle losses

# place holder for Coster's SIG parameter, anomalous conductivity

# com.sx # base 0,   (0:nx+1,0:ny+1)
mdsput(":sx","build_signal[build_with_units[$,""m2""],,]",com.sx[0:com.nx,]) # base 0,   (0:nx+1,0:ny+1)
mdsput(":sx:basisname","data($)","com.sx[0:com.nx,]") # base 0,   (0:nx+1,0:ny+1)
mdsput(":sx:comment","data($)","area of east face of primary cells [grd.m^2]") # base 0,   (0:nx+1,0:ny+1)

# com.sy # base 0,   (0:nx+1,0:ny+1)
mdsput(":sy","build_signal[build_with_units[$,""m2""],,]",com.sy[,0:com.ny]) # base 0,   (0:nx+1,0:ny+1)
mdsput(":sy:basisname","data($)","com.sy[,0:com.ny]") # base 0,   (0:nx+1,0:ny+1)
mdsput(":sy:comment","data($)","area of north face of primary cells [grd.m^2]") # base 0,   (0:nx+1,0:ny+1)

# place holder for Coster's TAB2 parameter, Neutral atom temperature

# Electron temperature
mdsput(":te","build_signal[build_with_units[$,""eV""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",bbb.te/bbb.qe) # base 0,   (0:nx+1,0:ny+1)
mdsput(":te:basisname","data($)","bbb.te/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(":te:comment","data($)","electron temperature in primary cell [eV]") # base 0,   (0:nx+1,0:ny+1)

# place holder for Coster's TEXTAN parameter, atom species

# place holder for Coster's TEXTCOMP parameter, Components

# place holder for Coster's TEXTIN parameter, Test ion species

# place holder for Coster's TEXTMN parameter, Molecular species

# Define species: 1=D0, 2=D+, 3=Imp0, 4,... = C+,++, ...
character*2 hydrogen[0:1]=["H0","H+"]
character*2 deuterium[0:1]=["D0","D+"]
character*2 tritium[0:1]=["T0","T+"]
character*4 helium[0:2]=["He0","He+","He2+"]
character*4 lithium[0:3]=["Li0","Li+","Li2+","Li3+"]
character*4 berllyium[0:4]=["Be0","Be+","Be2+","Be3+","Be4+"]
character*3 boron[0:5]=["B0","B+","B2+","B3+","B4+","B5+"]
character*3 carbon[0:6]=["C0","C+","C2+","C3+","C4+","C5+","C6+"]
character*3 nitrogen[0:7]=["N0","N+","N2+","N3+","N4+","N5+","N6+","N7+"]
character*3 oxygen[0:8]=["O0","O+","O2+","O3+","O4+","O5+","O6+","O7+", \
 "O8+"]
character*3 fluorine[0:9]=["F0","F+","F2+","F3+","F4+","F5+","F6+","F7+", \
   "F8+","F9+"]
character*5 neon[0:10]=["Ne0","Ne+","Ne2+","Ne3+","Ne4+","Ne5+","Ne6+", \
"Ne7+","Ne8+","Ne9+","Ne10+"]

# Assume first neutral and ion species is an isotope of hydrogen
if [bbb.znucl[1]==1] then
if [bbb.minu[1] .eq. 1.] then
character*5 textpl[ns]=hydrogen
elseif [bbb.minu[1] .eq. 2.] then
character*5 textpl[ns]=deuterium
elseif [bbb.minu[1] .eq. 3.] then
character*5 textpl[ns]=tritium
endif
else
remark "First species is not bbb.a hydrogen isotope!"
mdsclose
mdsdisconnect
call kaboom[-1]
endif

if [bbb.isimpon .gt. 5] then
integer nsm1=2*com.nhgsp
do ii=com.nhgsp+1,com.ngsp
integer jz=ii-com.nhgsp
if [bbb.znucl[nsm1+1] .eq. 2] then
textpl=[textpl[1:nsm1],helium[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 3] then
textpl=[textpl[1:nsm1],lithium[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 4] then
textpl=[textpl[1:nsm1],berllyium[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 5] then
textpl=[textpl[1:nsm1],boron[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 6] then
textpl=[textpl[1:nsm1],carbon[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 7] then
textpl=[textpl[1:nsm1],nitrogen[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 8] then
textpl=[textpl[1:nsm1],oxygen[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 9] then
textpl=[textpl[1:nsm1],fluorine[0:com.nzsp[jz]]]
elseif [bbb.znucl[nsm1+1] .eq. 10] then
textpl=[textpl[1:nsm1],neon[0:com.nzsp[jz]]]
else
remark "Impurity species is greater than Ne!"
mdsclose
mdsdisconnect
call kaboom[-1]
endif
nsm1=nsm1+com.nzsp[jz]+1
enddo
endif

mdsput(".textpl","data($)",textpl)
mdsput(".textpl:basisname","data($)","no corresponding BASIS variable")
mdsput(".textpl:comment","data($)","ion/neutral species")

# Ion temperature [UEDGE: all ions at same temperature]
mdsput(":ti","build_signal[build_with_units[$,""eV""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz]",bbb.ti/bbb.qe) # base 0,   (0:nx+1,0:ny+1)
mdsput(":ti:basisname","data($)","bbb.ti/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(":ti:comment","data($)","Ion temperature in primary cell [eV]") # base 0,   (0:nx+1,0:ny+1)

# place holder for Coster's TIB2 parameter, Test ion temperature

# place holder for Coster's TMB2 parameter, Neutral molecule temperature

# [Neutral]/Ion parallel velocity
# Diffusive neutral carbon model, hence set carbon neutral velocity to api.zero
real ua[0:com.nx,0:com.ny+1,ns]
integer bbb.igsp,ifld,ii
if [com.nhgsp .gt. 1] then
remark "Not implemented for more than api.one hydrogen species!"
call kaboom[-1]
endif
ua[,,1]=0.
if [bbb.isupgon[1] .eq. 1] ua[,,1]=bbb.upi[0:com.nx,,bbb.iigsp] # base 0,   (0:nx+1,0:ny+1,1:nisp)
ua[,,2]=bbb.upi[0:com.nx,,1] # base 0,   (0:nx+1,0:ny+1,1:nisp)

if [bbb.isimpon .ge. 5] then  # multi species impurities
integer nsm1=2*com.nhgsp
do bbb.igsp=com.nhgsp+1,com.ngsp
integer jz=bbb.igsp-com.nhgsp
ua[,,nsm1+jz]=0.   # impurity neutrals are diffusive
do ifld=1,com.nzsp[jz]
ua[,,nsm1+jz+ifld]=bbb.upi[0:com.nx,,nsm1+ifld] # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo
nsm1=nsm1+com.nzsp[jz]
enddo
endif

mdsput(":ua","build_signal[build_with_units[$,""grd.m/s""],,\top.snapshot.grid:cr,\top.snapshot.grid:cz,\top.snapshot:textpl]",ua)
mdsput(":ua:basisname","data($)","bbb.upi") # base 0,   (0:nx+1,0:ny+1,1:nisp)
mdsput(".ua:comment","data($)","neutral/ion parallel velocity in primary cell [grd.m/s]")

# place holder for Coster's VISC parameter, Viscosity

# place holder for Coster's VLAX parameter, Poloidal pinch velocity

# place holder for Coster's VLAY parameter, Radial pinch velocity

# volume
mdsput(":com.vol:basisname","data($)","com.vol") # base 0,   (0:nx+1,0:ny+1)
mdsput(":com.vol","build_signal[build_with_units[$,""m3""],,]",com.vol) # base 0,   (0:nx+1,0:ny+1)
mdsput(":com.vol:comment","data($)","Volume of primary cells [grd.m^3]") # base 0,   (0:nx+1,0:ny+1)

# end of SNAPSHOT branch
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# store IDENT branch

mdssetdefault["\top.ident"]

# place holder for Coster's parameter B2FGMTRYID, md5sum hash of b2fgmtry

# place holder for Coster's parameter B2FPLAMSAID, md5sum hash of b2fplasma

# place holder for Coster's parameter B2FSTATEID, md5sum hash of b2fstate

# place holder for Coster's parameter BWFSTATIID, md5sum hash of b2stati

# Date written to database
character*8 date=infodate
mdsput(":date","data($)",date)
mdsput(".date:comment","data($)","Date information written to MDSplus")

# Directory in which the run was stored [GDP]
basisexe["pwd > pwd.txt"]
integer unit=basopen["pwd.txt","r"]
character*80 rundir
basreadline[unit,&rundir]
basclose[unit]
rundir=trim[rundir]
#!com.rm pwd.txt # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".directory","data($)",rundir)
mdsput(".directory:comment","data($)","Directory used for save files, etc.")

# Identity for Experiment
if [exists["machine"]] then
mdsput(":exp","data($)",machine)
mdsput(".exp:comment","data($)","Experiment name")
else
mdsput(":exp","data($)","n/bbb.a")
mdsput(".exp:comment","data($)","Experiment name not specified")
endif

# Geometry
mdsput(":com.geometry","data($)",com.geometry)
mdsput(".com.geometry:basisname","data($)","com.geometry")
mdsput(".com.geometry:comment","data($)","mnemonic for com.geometry")

# Host identification
character*10 temp=infohost
mdsput(":host","data($)",temp)
mdsput(".host:comment","data($)","host running on when write to MDSplus")

# place holder for Coster's parameter MAIN, Label in b2fstate derived from b2mn.dat

# Number of UEDGE fluid species
mdsput(".ns","data($)",ns)
mdsput(".ns:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".ns:comment","data($)","Number of species")

# Grid size in poloidal direction, including guard cells
mdsput(".com.nx","data($)",com.nx+2)
mdsput(".com.nx:basisname","data($)","com.nx+2")
mdsput(".com.nx:comment","data($)","Number of poloidal cells")

# Grid size in radial direction, including guard cells
mdsput(".com.ny","data($)",com.ny+2)
mdsput(".com.ny:basisname","data($)","com.ny+2")
mdsput(".com.ny:comment","data($)","Number of radial cells")

# place holder for Coster's parameter OBJECTCODE

# place holder for Coster's parameter PHYSICS

# Problem name
mdsput(".probname","data($)",probname)

mdsput(":shot","data($)",com.eshot)
mdsput(".shot:basisname","data($)","com.eshot")
mdsput(".shot:comment","data($)","Experiment shot number")

# List of plasma species
# concatenate components of textpl to form Coster's character string
character*5 cstrspcs=textpl[1]
integer ii
do ii=2,ns
integer iii=ii*5
character*iii cstrspcs=cstrspcs//textpl[ii]
enddo
mdsput(".species","data($)",cstrspcs)
mdsput(".species:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".species:comment","data($)","Character string of plasma species")

real temp=com.etime*1.e-3
mdsput(":time","data($)",temp)
mdsput(".time:basisname","data($)","com.etime*1.e-3")
mdsput(".time:comment","data($)","Experiment shot time [s]")

# place holder for Coster's parameter UEDGETOP

mdsput(":uedgeversion","data($)",bbb.uedge_ver)
mdsput(".uedgeversion:basisname","data($)","bbb.uedge_ver")
mdsput(".uedgeversion:comment","data($)","UEDGE version number")

# user [GDP]
#!whoami > pwd.txt
integer unit=basopen["pwd.txt","r"]
character*80 whoami
basreadline[unit,&whoami]
basclose[unit]
whoami=trim[whoami]
#!com.rm pwd.txt # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".user","data($)",whoami)
mdsput(".user:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".user:comment","data($)","User running code when MDSPLUS data written")

# place holder for Coster's parameter VERSION, version number of this routine

#character*6 temp=infocpu
#mdsput(":cpu","data($)",temp)
#mdsput(".cpu:comment","data($)","CPU running on when write to MDSplus")

# ------------------------------------------------------------------------
# store IDENT.IMPSEP

# Inner midplane separatrix R
mdsput(".impsep:cr","data($)",com.rm[iximp,com.iysptrx,0]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".impsep.cr:basisname","data($)","com.rm[iximp,com.iysptrx,0]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".impsep.cr:comment","data($)","Separatrix radius at IMP [grd.m]")

# Inner midplane separatrix Z
mdsput(".impsep:cz","data($)",com.zm[iximp,com.iysptrx,0]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".impsep.cz:basisname","data($)","com.zm[iximp,com.iysptrx,0]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".impsep.cz:comment","data($)","Separatrix vertical position at IMP [grd.m]")

# Inner midplane separatrix diffusion coefficient 
mdsput(".impsep:d","data($)",bbb.difni[1])
mdsput(".impsep:d:basisname","data($)","bbb.difni[1]")
mdsput(".impsep:d:comment","data($)","diffusion coefficient [m2/s]")

# Inner midplane separatrix electron bbb.diffusivity # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:kye","data($)",bbb.kye)
mdsput(".impsep:kye:basisname","data($)","bbb.kye")
mdsput(".impsep:kye:comment","data($)","electron thermal diffusicity [m2/s]")

# Inner midplane separatix ion bbb.diffusivity for ns=1 # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:kyi","data($)",bbb.kyi)
mdsput(".impsep:kyi:basisname","data($)","bbb.kyi")
mdsput(".impsep:kyi:comment","data($)","ion thermal diffusicity [m2/s]")

# Inner midplane separatrix ion/atom bbb.diffusivity # base 0,   (0:nx+1,0:ny+1)
# mdsput(".impsep:kyi0","data($)",???)

# Inner midplane separatrix bbb.ne # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:ne","data($)",bbb.ne[iximp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:ne:basisname","data($)","bbb.ne[iximp,com.iysptrx]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:ne:comment","data($)","Electron density at IMP separatrix [grd.m^-3]") # base 0,   (0:nx+1,0:ny+1)

# Inner midplane separatrix Te [eV]
mdsput(".impsep:te","data($)",1./bbb.qe*bbb.te[iximp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:te:basisname","data($)","bbb.te[iximp,com.iysptrx]/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:te:comment","data($)","Electron temperature at IMP separatrix, [eV]") # base 0,   (0:nx+1,0:ny+1)

# Inner midplane separatrix Ti [eV]
mdsput(".impsep:ti","data($)",1./bbb.qe*bbb.ti[iximp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:ti:basisname","data($)","bbb.ti[iximp,com.iysptrx]/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(".impsep:ti:comment","data($)","Ion temperature at IMP separatrix, [eV]") # base 0,   (0:nx+1,0:ny+1)

# end of IDENT.IMPSEP branch
# --------------------------------------------------------------------------

# ------------------------------------------------------------------------
# store IDENT.OMPSEP branch

# Outer midplane separatrix R
mdsput(".ompsep:cr","data($)",com.rm[bbb.ixmp,com.iysptrx,0]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".ompsep.cr:basisname","data($)","com.rm[bbb.ixmp,com.iysptrx,0]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".ompsep.cr:comment","data($)","Separatrix radius at OMP [grd.m]")

# Outer midplane separatrix Z
mdsput(".ompsep:cz","data($)",com.zm[bbb.ixmp,com.iysptrx,0]) # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".ompsep.cz:basisname","data($)","com.zm[bbb.ixmp,com.iysptrx,0]") # base 0,   (0:nxm+1,0:nym+1,0:4)
mdsput(".ompsep.cz:comment","data($)","Separatrix vertical position at OMP [grd.m]")

# Outer midplane separatrix diffusion coefficient 
mdsput(".ompsep:d","data($)",bbb.difni[1])
mdsput(".ompsep:d:basisname","data($)","bbb.difni[1]")
mdsput(".ompsep:d:comment","data($)","diffusion coefficient [m2/s]")

# Outer midplane separatrix electron bbb.diffusivity # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:kye","data($)",bbb.kye)
mdsput(".ompsep:kye:basisname","data($)","bbb.kye")
mdsput(".ompsep:kye:comment","data($)","electron thermal diffusicity [m2/s]")

# Outer midplane separatix ion diffusivityt for ns=1
mdsput(".ompsep:kyi","data($)",bbb.kyi)
mdsput(".impsep:kyi:basisname","data($)","bbb.kyi")
mdsput(".impsep:kyi:comment","data($)","ion thermal diffusicity [m2/s]")

# Outer midplane separatrix ion/atom bbb.diffusivity # base 0,   (0:nx+1,0:ny+1)
# mdsput(".ompsep:kyi0","data($)",???)

# Outer midplane separatrix bbb.ne # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:ne","data($)",bbb.ne[bbb.ixmp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:ne:basisname","data($)","bbb.ne[bbb.ixmp,com.iysptrx]") # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:ne:comment","data($)","Electron density at OMP separatrix [grd.m^-3]") # base 0,   (0:nx+1,0:ny+1)

# Outer midplane separatrix Te [eV]
mdsput(".ompsep:te","data($)",1./bbb.qe*bbb.te[bbb.ixmp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:te:basisname","data($)","bbb.te[bbb.ixmp,com.iysptrx]/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:te:comment","data($)","Electron temperature at OMP separatrix, [eV]") # base 0,   (0:nx+1,0:ny+1)

# Outer midplane separatrix Ti [eV]
mdsput(".ompsep:ti","data($)",1./bbb.qe*bbb.ti[bbb.ixmp,com.iysptrx]) # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:ti:basisname","data($)","bbb.ti[bbb.ixmp,com.iysptrx]/aph.bbb.ev") # base 0,   (0:nx+1,0:ny+1)
mdsput(".ompsep:ti:comment","data($)","Ion temperature at OMP separatrix, [eV]") # base 0,   (0:nx+1,0:ny+1)

# end of IDENT.OMPSEP branch
# --------------------------------------------------------------------------

# ------------------------------------------------------------------------
# store IDENT.SEP

# Core-SOL electron energy flow [W]
real fhe=par.sum[bbb.feey[com.ixpt1+1:com.ixpt2,com.iysptrx]] # base 0,   (0:nx+1,0:ny+1)
mdsput(".sep:fhe","data($)",fhe)
mdsput(".sep:fhe:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".sep:fhe:comment","data($)","electron energy flow across separatrix [W]")

# Core-SOL ion energy flow [W]
real fhi=par.sum[bbb.feiy[com.ixpt1+1:com.ixpt2,com.iysptrx]] # base 0,   (0:nx+1,0:ny+1)
mdsput(".sep:fhi","data($)",fhi)
mdsput(".sep:fhi:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".sep:fhi:comment","data($)","Ion energy flow across separatrix [W]")

# Core-SOL electron flow [W] [per GDP]
real fne[0:com.nx+1,1:com.nisp]
do ii=1,com.nisp
fne[0:com.nx+1,ii]=bbb.fniy[,com.iysptrx,ii]*api.bbb.zi[ii]-bbb.fqy[,com.iysptrx]/bbb.qe # base 0,   (0:nx+1,0:ny+1) # base 0,   (0:nx+1,0:ny+1,1:nisp)
enddo
mdsput(".sep:fne","data($)",par.sum[fne[com.ixpt1+1:com.ixpt2,]])
mdsput(".sep:fne:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".sep:fne:comment","data($)","Electron flux across separatrix [/s]")

# Core-SOL ion flow [W]
real fni=par.sum[bbb.fniy[com.ixpt1+1:com.ixpt2,com.iysptrx,1:com.nisp]] # base 0,   (0:nx+1,0:ny+1,1:nisp)
mdsput(".sep:fni","data($)",fni)
mdsput(".sep:fni:basisname","data($)","bbb.see write_uedge2mds") # base 0,   (0:nx+1,0:ny+1,1:nstra)
mdsput(".sep:fni:comment","data($)","Ion flux across separatrix [/s]")

# End of IDENT branch
# ------------------------------------------------------------------------

# Now write MDSplus tree and disconnect

mdstcl["write"]

mdsclose
mdsdisconnect
remark "data written to shot "//shot_s

outtree.write()
outtree.close()
