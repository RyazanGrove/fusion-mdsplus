import MDSplus

def compare_trees(first_tree, second_tree):
    difference_count = 0

    #open first tree
    tree1 = MDSplus.Tree("uedge", first_tree)
    #open second treee
    tree2 = MDSplus.Tree("uedge", second_tree)
    
    # -------------------------------------------------------------------------
    # store SNAPSHOT.DIMENSIONS 

    #SNAPSHOT.DIMENSIONS.IMP.data())
    if tree1.SNAPSHOT.DIMENSIONS.IMP.data() != tree2.SNAPSHOT.DIMENSIONS.IMP.data():
        print("SNAPSHOT.DIMENSIONS.IMP are different") 
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.IMP.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.IMP.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.IMP.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.IMP.COMMENT are different")
        difference_count += 1
    
    #SNAPSHOT.DIMENSIONS.IMP.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.IMP.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.IMP.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.IMP.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NATM.data
    if tree1.SNAPSHOT.DIMENSIONS.NATM.data() != tree2.SNAPSHOT.DIMENSIONS.NATM.data():
        print("SNAPSHOT.DIMENSIONS.NATM are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NATM.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.NATM.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.NATM.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.NATM.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NATM.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.NATM.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.NATM.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.NATM.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NS.data
    if tree1.SNAPSHOT.DIMENSIONS.NS.data() != tree2.SNAPSHOT.DIMENSIONS.NS.data():
        print("SNAPSHOT.DIMENSIONS.NS are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NS.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.NS.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.NS.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.NS.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NS.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.NS.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.NS.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.NS.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NX.data
    if tree1.SNAPSHOT.DIMENSIONS.NX.data() != tree2.SNAPSHOT.DIMENSIONS.NX.data():
        print("SNAPSHOT.DIMENSIONS.NX are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NX.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.NX.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.NX.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.NX.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NX.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.NX.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.NX.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.NX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NY.data
    if tree1.SNAPSHOT.DIMENSIONS.NY.data() != tree2.SNAPSHOT.DIMENSIONS.NY.data():
        print("SNAPSHOT.DIMENSIONS.NY are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NY.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.NY.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.NY.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.NY.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.NY.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.NY.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.NY.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.NY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.OMP.data
    if tree1.SNAPSHOT.DIMENSIONS.OMP.data() != tree2.SNAPSHOT.DIMENSIONS.OMP.data():
        print("SNAPSHOT.DIMENSIONS.OMP are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.OMP.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.OMP.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.OMP.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.OMP.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.OMP.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.OMP.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.OMP.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.OMP.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.SEP.data
    if tree1.SNAPSHOT.DIMENSIONS.SEP.data() != tree2.SNAPSHOT.DIMENSIONS.SEP.data():
        print("SNAPSHOT.DIMENSIONS.SEP are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.SEP.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.SEP.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.SEP.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.SEP.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.SEP.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.SEP.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.SEP.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.SEP.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG1.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG1.data() != tree2.SNAPSHOT.DIMENSIONS.TARG1.data():
        print("SNAPSHOT.DIMENSIONS.TARG1 are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG1.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG1.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.TARG1.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.TARG1.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG1.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG1.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.TARG1.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.TARG1.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG2.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG2.data() != tree2.SNAPSHOT.DIMENSIONS.TARG2.data():
        print("SNAPSHOT.DIMENSIONS.TARG2 are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG2.BASISNAME.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG2.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.TARG2.BASISNAME.data():
        print("SNAPSHOT.DIMENSIONS.TARG2.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.DIMENSIONS.TARG2.COMMENT.data
    if tree1.SNAPSHOT.DIMENSIONS.TARG2.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.TARG2.COMMENT.data():
        print("SNAPSHOT.DIMENSIONS.TARG2.COMMENT are different")
        difference_count += 1
    
    try:
        #SNAPSHOT.DIMENSIONS.TARG3.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG3.data() != tree2.SNAPSHOT.DIMENSIONS.TARG3.data():
            print("SNAPSHOT.DIMENSIONS.TARG3 are different")
            difference_count += 1

        #SNAPSHOT.DIMENSIONS.TARG3.BASISNAME.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG3.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.TARG3.BASISNAME.data():
            print("SNAPSHOT.DIMENSIONS.TARG3.BASISNAME are different")
            difference_count += 1

        #SNAPSHOT.DIMENSIONS.TARG3.COMMENT.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG3.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.TARG3.COMMENT.data():
            print("SNAPSHOT.DIMENSIONS.TARG3.COMMENT are different")
            difference_count += 1
    except MDSplus.mdsExceptions.TreeNODATA as ex:
        print("No data in SNAPSHOT.DIMENSIONS.TARG3.data")

    try:
        #SNAPSHOT.DIMENSIONS.TARG4.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG4.data() != tree2.SNAPSHOT.DIMENSIONS.TARG4.data():
            print("SNAPSHOT.DIMENSIONS.TARG4 are different")
            difference_count += 1

        #SNAPSHOT.DIMENSIONS.TARG4.BASISNAME.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG4.BASISNAME.data() != tree2.SNAPSHOT.DIMENSIONS.TARG4.BASISNAME.data():
            print("SNAPSHOT.DIMENSIONS.TARG4.BASISNAME are different")
            difference_count += 1

        #SNAPSHOT.DIMENSIONS.TARG4.COMMENT.data
        if tree1.SNAPSHOT.DIMENSIONS.TARG4.COMMENT.data() != tree2.SNAPSHOT.DIMENSIONS.TARG4.COMMENT.data():
            print("SNAPSHOT.DIMENSIONS.TARG4.COMMENT are different")
            difference_count += 1
    except MDSplus.mdsExceptions.TreeNODATA as ex:
        print("No data in SNAPSHOT.DIMENSIONS.TARG4.data")

    # end of SNAPSHOT.DIMENSIONS
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # store SNAPSHOT.GRID


    #SNAPSHOT.GRID.AM.data
    if not (tree1.SNAPSHOT.GRID.AM.data() == tree2.SNAPSHOT.GRID.AM.data()).all():
        print("SNAPSHOT.GRID.AM are different")
        difference_count += 1

    #SNAPSHOT.GRID.AM.BASISNAME.data
    if tree1.SNAPSHOT.GRID.AM.BASISNAME.data() != tree2.SNAPSHOT.GRID.AM.BASISNAME.data():
        print("SNAPSHOT.GRID.AM.BASISNAME are different")
        difference_count += 1

    #SNAPSHOT.GRID.AM.COMMENT.data
    if tree1.SNAPSHOT.GRID.AM.COMMENT.data() != tree2.SNAPSHOT.GRID.AM.COMMENT.data():
        print("SNAPSHOT.GRID.AM.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.RIGHTIX.data
    if not (tree1.SNAPSHOT.GRID.RIGHTIX.data() == tree2.SNAPSHOT.GRID.RIGHTIX.data()).all():
        print("SNAPSHOT.GRID.RIGHTIX are different")
        difference_count += 1

    #SNAPSHOT.GRID.RIGHTIX.BASISNAME.data
    if tree1.SNAPSHOT.GRID.RIGHTIX.BASISNAME.data() != tree2.SNAPSHOT.GRID.RIGHTIX.BASISNAME.data():
        print("SNAPSHOT.GRID.RIGHTIX.BASISNAME are different")

    #SNAPSHOT.GRID.RIGHTIY.data
    if not (tree1.SNAPSHOT.GRID.RIGHTIY.data() == tree2.SNAPSHOT.GRID.RIGHTIY.data()).all():
        print("SNAPSHOT.GRID.RIGHTIY are different")
        difference_count += 1

    #SNAPSHOT.GRID.RIGHTIY.BASISNAME.data
    if tree1.SNAPSHOT.GRID.RIGHTIY.BASISNAME.data() != tree2.SNAPSHOT.GRID.RIGHTIY.BASISNAME.data():
        print("SNAPSHOT.GRID.RIGHTIY.BASISNAME are different")

    #SNAPSHOT.GRID.LEFTIX.data
    if not (tree1.SNAPSHOT.GRID.LEFTIX.data() == tree2.SNAPSHOT.GRID.LEFTIX.data()).all():
        print("SNAPSHOT.GRID.LEFTIX are different")
        difference_count += 1

    #SNAPSHOT.GRID.LEFTIX.BASISNAME.data
    if tree1.SNAPSHOT.GRID.LEFTIX.BASISNAME.data() != tree2.SNAPSHOT.GRID.LEFTIX.BASISNAME.data():
        print("SNAPSHOT.GRID.LEFTIX.BASISNAME are different")

    #SNAPSHOT.GRID.LEFTIY.data
    if not (tree1.SNAPSHOT.GRID.LEFTIY.data() == tree2.SNAPSHOT.GRID.LEFTIY.data()).all():
        print("SNAPSHOT.GRID.LEFTIY are different")
        difference_count += 1

    #SNAPSHOT.GRID.LEFTIY.BASISNAME.data
    if tree1.SNAPSHOT.GRID.LEFTIY.BASISNAME.data() != tree2.SNAPSHOT.GRID.LEFTIY.BASISNAME.data():
        print("SNAPSHOT.GRID.LEFTIY.BASISNAME are different")

    #SNAPSHOT.GRID.TOPIX.data
    if not (tree1.SNAPSHOT.GRID.TOPIX.data() == tree2.SNAPSHOT.GRID.TOPIX.data()).all():
        print("SNAPSHOT.GRID.TOPIX are different")
        difference_count += 1

    #SNAPSHOT.GRID.TOPIX.BASISNAME.data
    if tree1.SNAPSHOT.GRID.TOPIX.BASISNAME.data() != tree2.SNAPSHOT.GRID.TOPIX.BASISNAME.data():
        print("SNAPSHOT.GRID.TOPIX.BASISNAME are different")

    #SNAPSHOT.GRID.TOPIY.data
    if not (tree1.SNAPSHOT.GRID.TOPIY.data() == tree2.SNAPSHOT.GRID.TOPIY.data()).all():
        print("SNAPSHOT.GRID.TOPIY are different")
        difference_count += 1

    #SNAPSHOT.GRID.TOPIY.BASISNAME.data
    if tree1.SNAPSHOT.GRID.TOPIY.BASISNAME.data() != tree2.SNAPSHOT.GRID.TOPIY.BASISNAME.data():
        print("SNAPSHOT.GRID.TOPIY.BASISNAME are different")

    #SNAPSHOT.GRID.BOTTOMIX.data
    if not (tree1.SNAPSHOT.GRID.BOTTOMIX.data() == tree2.SNAPSHOT.GRID.BOTTOMIX.data()).all():
        print("SNAPSHOT.GRID.BOTTOMIX are different")
        difference_count += 1

    #SNAPSHOT.GRID.BOTTOMIX.BASISNAME.data
    if tree1.SNAPSHOT.GRID.BOTTOMIX.BASISNAME.data() != tree2.SNAPSHOT.GRID.BOTTOMIX.BASISNAME.data():
        print("SNAPSHOT.GRID.BOTTOMIX.BASISNAME are different")

    #SNAPSHOT.GRID.BOTTOMIY.data
    if not (tree1.SNAPSHOT.GRID.BOTTOMIY.data() == tree2.SNAPSHOT.GRID.BOTTOMIY.data()).all():
        print("SNAPSHOT.GRID.BOTTOMIY are different")
        difference_count += 1

    #SNAPSHOT.GRID.BOTTOMIY.BASISNAME.data
    if tree1.SNAPSHOT.GRID.BOTTOMIY.BASISNAME.data() != tree2.SNAPSHOT.GRID.BOTTOMIY.BASISNAME.data():
        print("SNAPSHOT.GRID.BOTTOMIY.BASISNAME are different")

    #SNAPSHOT.GRID.CR.data
    if not (tree1.SNAPSHOT.GRID.CR.data() == tree2.SNAPSHOT.GRID.CR.data()).all():
        print("SNAPSHOT.GRID.CR are different")
        difference_count += 1

    #SNAPSHOT.GRID.CR.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CR.BASISNAME.data() != tree2.SNAPSHOT.GRID.CR.BASISNAME.data():
        print("SNAPSHOT.GRID.CR.BASISNAME are different")

    #SNAPSHOT.GRID.CR.COMMENT.data
    if tree1.SNAPSHOT.GRID.CR.COMMENT.data() != tree2.SNAPSHOT.GRID.CR.COMMENT.data():
        print("SNAPSHOT.GRID.CR.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.PSIN.data
    if not (tree1.SNAPSHOT.GRID.PSIN.data() == tree2.SNAPSHOT.GRID.PSIN.data()).all():
        print("SNAPSHOT.GRID.PSIN are different")
        difference_count += 1

    #SNAPSHOT.GRID.PSIN.BASISNAME.data
    if tree1.SNAPSHOT.GRID.PSIN.BASISNAME.data() != tree2.SNAPSHOT.GRID.PSIN.BASISNAME.data():
        print("SNAPSHOT.GRID.PSIN.BASISNAME are different")

    #SNAPSHOT.GRID.PSIN.COMMENT.data
    if tree1.SNAPSHOT.GRID.PSIN.COMMENT.data() != tree2.SNAPSHOT.GRID.PSIN.COMMENT.data():
        print("SNAPSHOT.GRID.PSIN.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.CR_X.data
    if not (tree1.SNAPSHOT.GRID.CR_X.data() == tree2.SNAPSHOT.GRID.CR_X.data()).all():
        print("SNAPSHOT.GRID.CR_X are different")
        difference_count += 1

    #SNAPSHOT.GRID.CR_X.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CR_X.BASISNAME.data() != tree2.SNAPSHOT.GRID.CR_X.BASISNAME.data():
        print("SNAPSHOT.GRID.CR_X.BASISNAME are different")

    #SNAPSHOT.GRID.CR_X.COMMENT.data
    if tree1.SNAPSHOT.GRID.CR_X.COMMENT.data() != tree2.SNAPSHOT.GRID.CR_X.COMMENT.data():
        print("SNAPSHOT.GRID.CR_X.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.CR_Y.data
    if not (tree1.SNAPSHOT.GRID.CR_Y.data() == tree2.SNAPSHOT.GRID.CR_Y.data()).all():
        print("SNAPSHOT.GRID.CR_Y are different")
        difference_count += 1
    
    #SNAPSHOT.GRID.CR_Y.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CR_Y.BASISNAME.data() != tree2.SNAPSHOT.GRID.CR_Y.BASISNAME.data():
        print("SNAPSHOT.GRID.CR_Y.BASISNAME are different")

    #SNAPSHOT.GRID.CR_Y.COMMENT.data
    if tree1.SNAPSHOT.GRID.CR_Y.COMMENT.data() != tree2.SNAPSHOT.GRID.CR_Y.COMMENT.data():
        print("SNAPSHOT.GRID.CR_Y.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.CZ_X.data
    if not (tree1.SNAPSHOT.GRID.CZ_X.data() == tree2.SNAPSHOT.GRID.CZ_X.data()).all():
        print("SNAPSHOT.GRID.CZ_X are different")
        difference_count += 1
    
    #SNAPSHOT.GRID.CZ_X.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CZ_X.BASISNAME.data() != tree2.SNAPSHOT.GRID.CZ_X.BASISNAME.data():
        print("SNAPSHOT.GRID.CZ_X.BASISNAME are different")

    #SNAPSHOT.GRID.CZ_X.COMMENT.data
    if tree1.SNAPSHOT.GRID.CZ_X.COMMENT.data() != tree2.SNAPSHOT.GRID.CZ_X.COMMENT.data():
        print("SNAPSHOT.GRID.CZ_X.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.CZ_Y.data
    if not (tree1.SNAPSHOT.GRID.CZ_Y.data() == tree2.SNAPSHOT.GRID.CZ_Y.data()).all():
        print("SNAPSHOT.GRID.CZ_Y are different")
        difference_count += 1
    
    #SNAPSHOT.GRID.CZ_Y.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CZ_Y.BASISNAME.data() != tree2.SNAPSHOT.GRID.CZ_Y.BASISNAME.data():
        print("SNAPSHOT.GRID.CZ_Y.BASISNAME are different")

    #SNAPSHOT.GRID.CZ_Y.COMMENT.data
    if tree1.SNAPSHOT.GRID.CZ_Y.COMMENT.data() != tree2.SNAPSHOT.GRID.CZ_Y.COMMENT.data():
        print("SNAPSHOT.GRID.CZ_Y.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSPAR.data
    if not (tree1.SNAPSHOT.GRID.DSPAR.data() == tree2.SNAPSHOT.GRID.DSPAR.data()).all():
        print("SNAPSHOT.GRID.DSPAR are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSPAR.BASISNAME.data
    if tree1.SNAPSHOT.GRID.DSPAR.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSPAR.BASISNAME.data():
        print("SNAPSHOT.GRID.DSPAR.BASISNAME are different")

    #SNAPSHOT.GRID.DSPAR.COMMENT.data
    if tree1.SNAPSHOT.GRID.DSPAR.COMMENT.data() != tree2.SNAPSHOT.GRID.DSPAR.COMMENT.data():
        print("SNAPSHOT.GRID.DSPAR.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSPOL.data
    if not (tree1.SNAPSHOT.GRID.DSPOL.data() == tree2.SNAPSHOT.GRID.DSPOL.data()).all():
        print("SNAPSHOT.GRID.DSPOL are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSPOL.BASISNAME.data
    if tree1.SNAPSHOT.GRID.DSPOL.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSPOL.BASISNAME.data():
        print("SNAPSHOT.GRID.DSPOL.BASISNAME are different")

    #SNAPSHOT.GRID.DSPOL.COMMENT.data
    if tree1.SNAPSHOT.GRID.DSPOL.COMMENT.data() != tree2.SNAPSHOT.GRID.DSPOL.COMMENT.data():
        print("SNAPSHOT.GRID.DSPOL.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSRAD.data
    if not (tree1.SNAPSHOT.GRID.DSRAD.data() == tree2.SNAPSHOT.GRID.DSRAD.data()).all():
        print("SNAPSHOT.GRID.DSRAD are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSRAD.BASISNAME.data
    if tree1.SNAPSHOT.GRID.DSRAD.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSRAD.BASISNAME.data():
        print("SNAPSHOT.GRID.DSRAD.BASISNAME are different")

    #SNAPSHOT.GRID.DSRAD.COMMENT.data
    if tree1.SNAPSHOT.GRID.DSRAD.COMMENT.data() != tree2.SNAPSHOT.GRID.DSRAD.COMMENT.data():
        print("SNAPSHOT.GRID.DSRAD.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSTARG1.data
    if not (tree1.SNAPSHOT.GRID.DSTARG1.data() == tree2.SNAPSHOT.GRID.DSTARG1.data()).all():
        print("SNAPSHOT.GRID.DSTARG1 are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSTARG1.BASISNAME.data
    if tree1.SNAPSHOT.GRID.DSTARG1.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSTARG1.BASISNAME.data():
        print("SNAPSHOT.GRID.DSTARG1.BASISNAME are different")

    #SNAPSHOT.GRID.DSTARG1.COMMENT.data
    if tree1.SNAPSHOT.GRID.DSTARG1.COMMENT.data() != tree2.SNAPSHOT.GRID.DSTARG1.COMMENT.data():
        print("SNAPSHOT.GRID.DSTARG1.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSTARG2.data
    if not (tree1.SNAPSHOT.GRID.DSTARG2.data() == tree2.SNAPSHOT.GRID.DSTARG2.data()).all():
        print("SNAPSHOT.GRID.DSTARG2 are different")
        difference_count += 1

    #SNAPSHOT.GRID.DSTARG2.BASISNAME.data
    if tree1.SNAPSHOT.GRID.DSTARG2.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSTARG2.BASISNAME.data():
        print("SNAPSHOT.GRID.DSTARG2.BASISNAME are different")

    #SNAPSHOT.GRID.DSTARG2.COMMENT.data
    if tree1.SNAPSHOT.GRID.DSTARG2.COMMENT.data() != tree2.SNAPSHOT.GRID.DSTARG2.COMMENT.data():
        print("SNAPSHOT.GRID.DSTARG2.COMMENT are different")
        difference_count += 1

    try:
        #SNAPSHOT.GRID.DSTARG3.data
        if not (tree1.SNAPSHOT.GRID.DSTARG3.data() != tree2.SNAPSHOT.GRID.DSTARG3.data().all()):
            print("SNAPSHOT.GRID.DSTARG3 are different")
            difference_count += 1

        #SNAPSHOT.GRID.DSTARG3.BASISNAME.data
        if tree1.SNAPSHOT.GRID.DSTARG3.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSTARG3.BASISNAME.data():
            print("SNAPSHOT.GRID.DSTARG3.BASISNAME are different")
            difference_count += 1

        #SNAPSHOT.GRID.DSTARG3.COMMENT.data
        if tree1.SNAPSHOT.GRID.DSTARG3.COMMENT.data() != tree2.SNAPSHOT.GRID.DSTARG3.COMMENT.data():
            print("SNAPSHOT.GRID.DSTARG3.COMMENT are different")
            difference_count += 1
    except MDSplus.mdsExceptions.TreeNODATA as ex:
        print("No data in SNAPSHOT.GRID.DSTARG3.data")

    try:
        #SNAPSHOT.GRID.DSTARG4.data
        if not (tree1.SNAPSHOT.GRID.DSTARG4.data() != tree2.SNAPSHOT.GRID.DSTARG4.data().all()):
            print("SNAPSHOT.GRID.DSTARG4 are different")
            difference_count += 1

        #SNAPSHOT.GRID.DSTARG4.BASISNAME.data
        if tree1.SNAPSHOT.GRID.DSTARG4.BASISNAME.data() != tree2.SNAPSHOT.GRID.DSTARG4.BASISNAME.data():
            print("SNAPSHOT.GRID.DSTARG4.BASISNAME are different")
            difference_count += 1

        #SNAPSHOT.GRID.DSTARG4.COMMENT.data
        if tree1.SNAPSHOT.GRID.DSTARG4.COMMENT.data() != tree2.SNAPSHOT.GRID.DSTARG4.COMMENT.data():
            print("SNAPSHOT.GRID.DSTARG4.COMMENT are different")
            difference_count += 1
    except MDSplus.mdsExceptions.TreeNODATA as ex:
        print("No data in SNAPSHOT.GRID.DSTARG4.data")

    #SNAPSHOT.GRID.PSINRAD.data
    if not (tree1.SNAPSHOT.GRID.PSINRAD.data() == tree2.SNAPSHOT.GRID.PSINRAD.data()).all():
        print("SNAPSHOT.GRID.PSINRAD are different")
        difference_count += 1

    #SNAPSHOT.GRID.PSINRAD.BASISNAME.data
    if tree1.SNAPSHOT.GRID.PSINRAD.BASISNAME.data() != tree2.SNAPSHOT.GRID.PSINRAD.BASISNAME.data():
        print("SNAPSHOT.GRID.PSINRAD.BASISNAME are different")

    #SNAPSHOT.GRID.PSINRAD.COMMENT.data
    if tree1.SNAPSHOT.GRID.PSINRAD.COMMENT.data() != tree2.SNAPSHOT.GRID.PSINRAD.COMMENT.data():
        print("SNAPSHOT.GRID.PSINRAD.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.REGVOL.data
    if not (tree1.SNAPSHOT.GRID.REGVOL.data() == tree2.SNAPSHOT.GRID.REGVOL.data()).all():
        print("SNAPSHOT.GRID.REGVOL are different")
        difference_count += 1

    #SNAPSHOT.GRID.REGVOL.BASISNAME.data
    if tree1.SNAPSHOT.GRID.REGVOL.BASISNAME.data() != tree2.SNAPSHOT.GRID.REGVOL.BASISNAME.data():
        print("SNAPSHOT.GRID.REGVOL.BASISNAME are different")

    #SNAPSHOT.GRID.REGVOL.COMMENT.data
    if tree1.SNAPSHOT.GRID.REGVOL.COMMENT.data() != tree2.SNAPSHOT.GRID.REGVOL.COMMENT.data():
        print("SNAPSHOT.GRID.REGVOL.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.CZ.data
    if not (tree1.SNAPSHOT.GRID.CZ.data() == tree2.SNAPSHOT.GRID.CZ.data()).all():
        print("SNAPSHOT.GRID.CZ are different")
        difference_count += 1

    #SNAPSHOT.GRID.CZ.BASISNAME.data
    if tree1.SNAPSHOT.GRID.CZ.BASISNAME.data() != tree2.SNAPSHOT.GRID.CZ.BASISNAME.data():
        print("SNAPSHOT.GRID.CZ.BASISNAME are different")

    #SNAPSHOT.GRID.CZ.COMMENT.data
    if tree1.SNAPSHOT.GRID.CZ.COMMENT.data() != tree2.SNAPSHOT.GRID.CZ.COMMENT.data():
        print("SNAPSHOT.GRID.CZ.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.R.data
    if not (tree1.SNAPSHOT.GRID.R.data() == tree2.SNAPSHOT.GRID.R.data()).all():
        print("SNAPSHOT.GRID.R are different")
        difference_count += 1

    #SNAPSHOT.GRID.R.BASISNAME.data
    if tree1.SNAPSHOT.GRID.R.BASISNAME.data() != tree2.SNAPSHOT.GRID.R.BASISNAME.data():
        print("SNAPSHOT.GRID.R.BASISNAME are different")

    #SNAPSHOT.GRID.R.COMMENT.data
    if tree1.SNAPSHOT.GRID.R.COMMENT.data() != tree2.SNAPSHOT.GRID.R.COMMENT.data():
        print("SNAPSHOT.GRID.R.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.Z.data
    if not (tree1.SNAPSHOT.GRID.Z.data() == tree2.SNAPSHOT.GRID.Z.data()).all():
        print("SNAPSHOT.GRID.Z are different")
        difference_count += 1

    #SNAPSHOT.GRID.Z.BASISNAME.data
    if tree1.SNAPSHOT.GRID.Z.BASISNAME.data() != tree2.SNAPSHOT.GRID.Z.BASISNAME.data():
        print("SNAPSHOT.GRID.Z.BASISNAME are different")

    #SNAPSHOT.GRID.Z.COMMENT.data
    if tree1.SNAPSHOT.GRID.Z.COMMENT.data() != tree2.SNAPSHOT.GRID.Z.COMMENT.data():
        print("SNAPSHOT.GRID.Z.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.VESSEL.data
    if not (tree1.SNAPSHOT.GRID.VESSEL.data() == tree2.SNAPSHOT.GRID.VESSEL.data()).all():
        print("SNAPSHOT.GRID.VESSEL are different")
        difference_count += 1

    #SNAPSHOT.GRID.VESSEL.BASISNAME.data
    if tree1.SNAPSHOT.GRID.VESSEL.BASISNAME.data() != tree2.SNAPSHOT.GRID.VESSEL.BASISNAME.data():
        print("SNAPSHOT.GRID.VESSEL.BASISNAME are different")

    #SNAPSHOT.GRID.VESSEL.COMMENT.data
    if tree1.SNAPSHOT.GRID.VESSEL.COMMENT.data() != tree2.SNAPSHOT.GRID.VESSEL.COMMENT.data():
        print("SNAPSHOT.GRID.VESSEL.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.ZA.data
    if not (tree1.SNAPSHOT.GRID.ZA.data() == tree2.SNAPSHOT.GRID.ZA.data()).all():
        print("SNAPSHOT.GRID.ZA are different")
        difference_count += 1

    #SNAPSHOT.GRID.ZA.BASISNAME.data
    if tree1.SNAPSHOT.GRID.ZA.BASISNAME.data() != tree2.SNAPSHOT.GRID.ZA.BASISNAME.data():
        print("SNAPSHOT.GRID.ZA.BASISNAME are different")

    #SNAPSHOT.GRID.ZA.COMMENT.data
    if tree1.SNAPSHOT.GRID.ZA.COMMENT.data() != tree2.SNAPSHOT.GRID.ZA.COMMENT.data():
        print("SNAPSHOT.GRID.ZA.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.GRID.ZN.data
    if not (tree1.SNAPSHOT.GRID.ZN.data() == tree2.SNAPSHOT.GRID.ZN.data()).all():
        print("SNAPSHOT.GRID.ZN are different")
        difference_count += 1

    #SNAPSHOT.GRID.ZN.BASISNAME.data
    if tree1.SNAPSHOT.GRID.ZN.BASISNAME.data() != tree2.SNAPSHOT.GRID.ZN.BASISNAME.data():
        print("SNAPSHOT.GRID.ZN.BASISNAME are different")

    #SNAPSHOT.GRID.ZN.COMMENT.data
    if tree1.SNAPSHOT.GRID.ZN.COMMENT.data() != tree2.SNAPSHOT.GRID.ZN.COMMENT.data():
        print("SNAPSHOT.GRID.ZN.COMMENT are different")
        difference_count += 1

    # end of SNAPSHOT.GRID
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # store SNAPSHOT branch

    #SNAPSHOT.B.data
    if not (tree1.SNAPSHOT.B.data() == tree2.SNAPSHOT.B.data()).all():
        print("SNAPSHOT.B are different")
        difference_count += 1

    #SNAPSHOT.B.BASISNAME.data
    if tree1.SNAPSHOT.B.BASISNAME.data() != tree2.SNAPSHOT.B.BASISNAME.data():
        print("SNAPSHOT.B.BASISNAME are different")

    #SNAPSHOT.B.COMMENT.data
    if tree1.SNAPSHOT.B.COMMENT.data() != tree2.SNAPSHOT.B.COMMENT.data():
        print("SNAPSHOT.B.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FCHX.data
    if not (tree1.SNAPSHOT.FCHX.data() == tree2.SNAPSHOT.FCHX.data()).all():
        print("SNAPSHOT.FCHX are different")
        difference_count += 1

    #SNAPSHOT.FCHX.BASISNAME.data
    if tree1.SNAPSHOT.FCHX.BASISNAME.data() != tree2.SNAPSHOT.FCHX.BASISNAME.data():
        print("SNAPSHOT.FCHX.BASISNAME are different")

    #SNAPSHOT.FCHX.COMMENT.data
    if tree1.SNAPSHOT.FCHX.COMMENT.data() != tree2.SNAPSHOT.FCHX.COMMENT.data():
        print("SNAPSHOT.FCHX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FCHY.data
    if not (tree1.SNAPSHOT.FCHY.data() == tree2.SNAPSHOT.FCHY.data()).all():
        print("SNAPSHOT.FCHY are different")
        difference_count += 1

    #SNAPSHOT.FCHY.BASISNAME.data
    if tree1.SNAPSHOT.FCHY.BASISNAME.data() != tree2.SNAPSHOT.FCHY.BASISNAME.data():
        print("SNAPSHOT.FCHY.BASISNAME are different")
    
    #SNAPSHOT.FCHY.COMMENT.data
    if tree1.SNAPSHOT.FCHY.COMMENT.data() != tree2.SNAPSHOT.FCHY.COMMENT.data():
        print("SNAPSHOT.FCHY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FHEX.data
    if not (tree1.SNAPSHOT.FHEX.data() == tree2.SNAPSHOT.FHEX.data()).all():
        print("SNAPSHOT.FHEX are different")
        difference_count += 1

    #SNAPSHOT.FHEX.BASISNAME.data
    if tree1.SNAPSHOT.FHEX.BASISNAME.data() != tree2.SNAPSHOT.FHEX.BASISNAME.data():
        print("SNAPSHOT.FHEX.BASISNAME are different")

    #SNAPSHOT.FHEX.COMMENT.data
    if tree1.SNAPSHOT.FHEX.COMMENT.data() != tree2.SNAPSHOT.FHEX.COMMENT.data():
        print("SNAPSHOT.FHEX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FHEY.data
    if not (tree1.SNAPSHOT.FHEY.data() == tree2.SNAPSHOT.FHEY.data()).all():
        print("SNAPSHOT.FHEY are different")
        difference_count += 1

    #SNAPSHOT.FHEY.BASISNAME.data
    if tree1.SNAPSHOT.FHEY.BASISNAME.data() != tree2.SNAPSHOT.FHEY.BASISNAME.data():
        print("SNAPSHOT.FHEY.BASISNAME are different")
    
    #SNAPSHOT.FHEY.COMMENT.data
    if tree1.SNAPSHOT.FHEY.COMMENT.data() != tree2.SNAPSHOT.FHEY.COMMENT.data():
        print("SNAPSHOT.FHEY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FHIX.data
    if not (tree1.SNAPSHOT.FHIX.data() == tree2.SNAPSHOT.FHIX.data()).all():
        print("SNAPSHOT.FHIX are different")
        difference_count += 1

    #SNAPSHOT.FHIX.BASISNAME.data
    if tree1.SNAPSHOT.FHIX.BASISNAME.data() != tree2.SNAPSHOT.FHIX.BASISNAME.data():
        print("SNAPSHOT.FHIX.BASISNAME are different")
    
    #SNAPSHOT.FHIX.COMMENT.data
    if tree1.SNAPSHOT.FHIX.COMMENT.data() != tree2.SNAPSHOT.FHIX.COMMENT.data():
        print("SNAPSHOT.FHIX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FHIY.data
    if not (tree1.SNAPSHOT.FHIY.data() == tree2.SNAPSHOT.FHIY.data()).all():
        print("SNAPSHOT.FHIY are different")
        difference_count += 1

    #SNAPSHOT.FHIY.BASISNAME.data
    if tree1.SNAPSHOT.FHIY.BASISNAME.data() != tree2.SNAPSHOT.FHIY.BASISNAME.data():
        print("SNAPSHOT.FHIY.BASISNAME are different")
    
    #SNAPSHOT.FHIY.COMMENT.data
    if tree1.SNAPSHOT.FHIY.COMMENT.data() != tree2.SNAPSHOT.FHIY.COMMENT.data():
        print("SNAPSHOT.FHIY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FMOX.data
    if not (tree1.SNAPSHOT.FMOX.data() == tree2.SNAPSHOT.FMOX.data()).all():
        print("SNAPSHOT.FMOX are different")
        difference_count += 1

    #SNAPSHOT.FMOX.BASISNAME.data
    if tree1.SNAPSHOT.FMOX.BASISNAME.data() != tree2.SNAPSHOT.FMOX.BASISNAME.data():
        print("SNAPSHOT.FMOX.BASISNAME are different")
    
    #SNAPSHOT.FMOX.COMMENT.data
    if tree1.SNAPSHOT.FMOX.COMMENT.data() != tree2.SNAPSHOT.FMOX.COMMENT.data():
        print("SNAPSHOT.FMOX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FMOY.data
    if not (tree1.SNAPSHOT.FMOY.data() == tree2.SNAPSHOT.FMOY.data()).all():
        print("SNAPSHOT.FMOY are different")
        difference_count += 1

    #SNAPSHOT.FMOY.BASISNAME.data
    if tree1.SNAPSHOT.FMOY.BASISNAME.data() != tree2.SNAPSHOT.FMOY.BASISNAME.data():
        print("SNAPSHOT.FMOY.BASISNAME are different")

    #SNAPSHOT.FMOY.COMMENT.data
    if tree1.SNAPSHOT.FMOY.COMMENT.data() != tree2.SNAPSHOT.FMOY.COMMENT.data():
        print("SNAPSHOT.FMOY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FNAX.data
    if not (tree1.SNAPSHOT.FNAX.data() == tree2.SNAPSHOT.FNAX.data()).all():
        print("SNAPSHOT.FNAX are different")
        difference_count += 1

    #SNAPSHOT.FNAX.BASISNAME.data
    if tree1.SNAPSHOT.FNAX.BASISNAME.data() != tree2.SNAPSHOT.FNAX.BASISNAME.data():
        print("SNAPSHOT.FNAX.BASISNAME are different")

    #SNAPSHOT.FNAX.COMMENT.data
    if tree1.SNAPSHOT.FNAX.COMMENT.data() != tree2.SNAPSHOT.FNAX.COMMENT.data():
        print("SNAPSHOT.FNAX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.FNAY.data
    if not (tree1.SNAPSHOT.FNAY.data() == tree2.SNAPSHOT.FNAY.data()).all():
        print("SNAPSHOT.FNAY are different")
        difference_count += 1

    #SNAPSHOT.FNAY.BASISNAME.data
    if tree1.SNAPSHOT.FNAY.BASISNAME.data() != tree2.SNAPSHOT.FNAY.BASISNAME.data():
        print("SNAPSHOT.FNAY.BASISNAME are different")

    #SNAPSHOT.FNAY.COMMENT.data
    if tree1.SNAPSHOT.FNAY.COMMENT.data() != tree2.SNAPSHOT.FNAY.COMMENT.data():
        print("SNAPSHOT.FNAY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.HX.data
    if not (tree1.SNAPSHOT.HX.data() == tree2.SNAPSHOT.HX.data()).all():
        print("SNAPSHOT.HX are different")
        difference_count += 1

    #SNAPSHOT.HX.BASISNAME.data
    if tree1.SNAPSHOT.HX.BASISNAME.data() != tree2.SNAPSHOT.HX.BASISNAME.data():
        print("SNAPSHOT.HX.BASISNAME are different")

    #SNAPSHOT.HX.COMMENT.data
    if tree1.SNAPSHOT.HX.COMMENT.data() != tree2.SNAPSHOT.HX.COMMENT.data():
        print("SNAPSHOT.HX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.HY.data
    if not (tree1.SNAPSHOT.HY.data() == tree2.SNAPSHOT.HY.data()).all():
        print("SNAPSHOT.HY are different")
        difference_count += 1

    #SNAPSHOT.HY.BASISNAME.data
    if tree1.SNAPSHOT.HY.BASISNAME.data() != tree2.SNAPSHOT.HY.BASISNAME.data():
        print("SNAPSHOT.HY.BASISNAME are different")

    #SNAPSHOT.HY.COMMENT.data
    if tree1.SNAPSHOT.HY.COMMENT.data() != tree2.SNAPSHOT.HY.COMMENT.data():
        print("SNAPSHOT.HY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.NA.data
    if not (tree1.SNAPSHOT.NA.data() == tree2.SNAPSHOT.NA.data()).all():
        print("SNAPSHOT.NA are different")
        difference_count += 1

    #SNAPSHOT.NA.BASISNAME.data
    if tree1.SNAPSHOT.NA.BASISNAME.data() != tree2.SNAPSHOT.NA.BASISNAME.data():
        print("SNAPSHOT.NA.BASISNAME are different")

    #SNAPSHOT.NA.COMMENT.data
    if tree1.SNAPSHOT.NA.COMMENT.data() != tree2.SNAPSHOT.NA.COMMENT.data():
        print("SNAPSHOT.NA.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.NE.data
    if not (tree1.SNAPSHOT.NE.data() == tree2.SNAPSHOT.NE.data()).all():
        print("SNAPSHOT.NE are different")
        difference_count += 1

    #SNAPSHOT.NE.BASISNAME.data
    if tree1.SNAPSHOT.NE.BASISNAME.data() != tree2.SNAPSHOT.NE.BASISNAME.data():
        print("SNAPSHOT.NE.BASISNAME are different")

    #SNAPSHOT.NE.COMMENT.data
    if tree1.SNAPSHOT.NE.COMMENT.data() != tree2.SNAPSHOT.NE.COMMENT.data():
        print("SNAPSHOT.NE.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.PR.data
    if not (tree1.SNAPSHOT.PR.data() == tree2.SNAPSHOT.PR.data()).all():
        print("SNAPSHOT.PR are different")
        difference_count += 1

    #SNAPSHOT.PR.BASISNAME.data
    if tree1.SNAPSHOT.PR.BASISNAME.data() != tree2.SNAPSHOT.PR.BASISNAME.data():
        print("SNAPSHOT.PR.BASISNAME are different")

    #SNAPSHOT.PR.COMMENT.data
    if tree1.SNAPSHOT.PR.COMMENT.data() != tree2.SNAPSHOT.PR.COMMENT.data():
        print("SNAPSHOT.PR.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.RQAHE.data
    if not (tree1.SNAPSHOT.RQAHE.data() == tree2.SNAPSHOT.RQAHE.data()).all():
        print("SNAPSHOT.RQAHE are different")
        difference_count += 1

    #SNAPSHOT.RQAHE.BASISNAME.data
    if tree1.SNAPSHOT.RQAHE.BASISNAME.data() != tree2.SNAPSHOT.RQAHE.BASISNAME.data():
        print("SNAPSHOT.RQAHE.BASISNAME are different")

    #SNAPSHOT.RQAHE.COMMENT.data
    if tree1.SNAPSHOT.RQAHE.COMMENT.data() != tree2.SNAPSHOT.RQAHE.COMMENT.data():
        print("SNAPSHOT.RQAHE.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.SX.data
    if not (tree1.SNAPSHOT.SX.data() == tree2.SNAPSHOT.SX.data()).all():
        print("SNAPSHOT.SX are different")
        difference_count += 1

    #SNAPSHOT.SX.BASISNAME.data
    if tree1.SNAPSHOT.SX.BASISNAME.data() != tree2.SNAPSHOT.SX.BASISNAME.data():
        print("SNAPSHOT.SX.BASISNAME are different")

    #SNAPSHOT.SX.COMMENT.data
    if tree1.SNAPSHOT.SX.COMMENT.data() != tree2.SNAPSHOT.SX.COMMENT.data():
        print("SNAPSHOT.SX.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.SY.data
    if not (tree1.SNAPSHOT.SY.data() == tree2.SNAPSHOT.SY.data()).all():
        print("SNAPSHOT.SY are different")
        difference_count += 1

    #SNAPSHOT.SY.BASISNAME.data
    if tree1.SNAPSHOT.SY.BASISNAME.data() != tree2.SNAPSHOT.SY.BASISNAME.data():
        print("SNAPSHOT.SY.BASISNAME are different")

    #SNAPSHOT.SY.COMMENT.data
    if tree1.SNAPSHOT.SY.COMMENT.data() != tree2.SNAPSHOT.SY.COMMENT.data():
        print("SNAPSHOT.SY.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.TE.data
    if not (tree1.SNAPSHOT.TE.data() == tree2.SNAPSHOT.TE.data()).all():
        print("SNAPSHOT.TE are different")
        difference_count += 1

    #SNAPSHOT.TE.BASISNAME.data
    if tree1.SNAPSHOT.TE.BASISNAME.data() != tree2.SNAPSHOT.TE.BASISNAME.data():
        print("SNAPSHOT.TE.BASISNAME are different")

    #SNAPSHOT.TE.COMMENT.data
    if tree1.SNAPSHOT.TE.COMMENT.data() != tree2.SNAPSHOT.TE.COMMENT.data():
        print("SNAPSHOT.TE.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.TEXTPL.data
    if tree1.SNAPSHOT.TEXTPL.data() != tree2.SNAPSHOT.TEXTPL.data():
        print("SNAPSHOT.TEXTPL are different")
        difference_count += 1

    #SNAPSHOT.TEXTPL.BASISNAME.data
    if tree1.SNAPSHOT.TEXTPL.BASISNAME.data() != tree2.SNAPSHOT.TEXTPL.BASISNAME.data():
        print("SNAPSHOT.TEXTPL.BASISNAME are different")

    #SNAPSHOT.TEXTPL.COMMENT.data
    if tree1.SNAPSHOT.TEXTPL.COMMENT.data() != tree2.SNAPSHOT.TEXTPL.COMMENT.data():
        print("SNAPSHOT.TEXTPL.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.TI.data
    if not (tree1.SNAPSHOT.TI.data() == tree2.SNAPSHOT.TI.data()).all():
        print("SNAPSHOT.TI are different")
        difference_count += 1

    #SNAPSHOT.TI.BASISNAME.data
    if tree1.SNAPSHOT.TI.BASISNAME.data() != tree2.SNAPSHOT.TI.BASISNAME.data():
        print("SNAPSHOT.TI.BASISNAME are different")

    #SNAPSHOT.TI.COMMENT.data
    if tree1.SNAPSHOT.TI.COMMENT.data() != tree2.SNAPSHOT.TI.COMMENT.data():
        print("SNAPSHOT.TI.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.UA.data
    if not (tree1.SNAPSHOT.UA.data() == tree2.SNAPSHOT.UA.data()).all():
        print("SNAPSHOT.UA are different")
        difference_count += 1

    #SNAPSHOT.UA.BASISNAME.data
    if tree1.SNAPSHOT.UA.BASISNAME.data() != tree2.SNAPSHOT.UA.BASISNAME.data():
        print("SNAPSHOT.UA.BASISNAME are different")

    #SNAPSHOT.UA.COMMENT.data
    if tree1.SNAPSHOT.UA.COMMENT.data() != tree2.SNAPSHOT.UA.COMMENT.data():
        print("SNAPSHOT.UA.COMMENT are different")
        difference_count += 1

    #SNAPSHOT.VOL.data
    if not (tree1.SNAPSHOT.VOL.data() == tree2.SNAPSHOT.VOL.data()).all():
        print("SNAPSHOT.VOL are different")
        difference_count += 1

    #SNAPSHOT.VOL.BASISNAME.data
    if tree1.SNAPSHOT.VOL.BASISNAME.data() != tree2.SNAPSHOT.VOL.BASISNAME.data():
        print("SNAPSHOT.VOL.BASISNAME are different")

    #SNAPSHOT.VOL.COMMENT.data
    if tree1.SNAPSHOT.VOL.COMMENT.data() != tree2.SNAPSHOT.VOL.COMMENT.data():
        print("SNAPSHOT.VOL.COMMENT are different")
        difference_count += 1

    # end of SNAPSHOT branch
    # --------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # store IDENT.IMPSEP

    #IDENT.IMPSEP.CR.data
    if tree1.IDENT.IMPSEP.CR.data() != tree2.IDENT.IMPSEP.CR.data():
        print("IDENT.IMPSEP.CR are different")
        difference_count += 1

    #IDENT.IMPSEP.CR.BASISNAME.data
    if tree1.IDENT.IMPSEP.CR.BASISNAME.data() != tree2.IDENT.IMPSEP.CR.BASISNAME.data():
        print("IDENT.IMPSEP.CR.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.CR.COMMENT.data
    if tree1.IDENT.IMPSEP.CR.COMMENT.data() != tree2.IDENT.IMPSEP.CR.COMMENT.data():
        print("IDENT.IMPSEP.CR.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.CZ.data
    if tree1.IDENT.IMPSEP.CZ.data() != tree2.IDENT.IMPSEP.CZ.data():
        print("IDENT.IMPSEP.CZ are different")
        difference_count += 1

    #IDENT.IMPSEP.CZ.BASISNAME.data
    if tree1.IDENT.IMPSEP.CZ.BASISNAME.data() != tree2.IDENT.IMPSEP.CZ.BASISNAME.data():
        print("IDENT.IMPSEP.CZ.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.CZ.COMMENT.data
    if tree1.IDENT.IMPSEP.CZ.COMMENT.data() != tree2.IDENT.IMPSEP.CZ.COMMENT.data():
        print("IDENT.IMPSEP.CZ.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.D.data
    if not (tree1.IDENT.IMPSEP.D.data() == tree2.IDENT.IMPSEP.D.data()).all():
        print("IDENT.IMPSEP.D are different")
        difference_count += 1

    #IDENT.IMPSEP.D.BASISNAME.data
    if tree1.IDENT.IMPSEP.D.BASISNAME.data() != tree2.IDENT.IMPSEP.D.BASISNAME.data():
        print("IDENT.IMPSEP.D.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.D.COMMENT.data
    if tree1.IDENT.IMPSEP.D.COMMENT.data() != tree2.IDENT.IMPSEP.D.COMMENT.data():
        print("IDENT.IMPSEP.D.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.KYE.data
    if tree1.IDENT.IMPSEP.KYE.data() != tree2.IDENT.IMPSEP.KYE.data():
        print("IDENT.IMPSEP.KYE are different")
        difference_count += 1

    #IDENT.IMPSEP.KYE.BASISNAME.data
    if tree1.IDENT.IMPSEP.KYE.BASISNAME.data() != tree2.IDENT.IMPSEP.KYE.BASISNAME.data():
        print("IDENT.IMPSEP.KYE.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.KYE.COMMENT.data
    if tree1.IDENT.IMPSEP.KYE.COMMENT.data() != tree2.IDENT.IMPSEP.KYE.COMMENT.data():
        print("IDENT.IMPSEP.KYE.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.KYI.data
    if tree1.IDENT.IMPSEP.KYI.data() != tree2.IDENT.IMPSEP.KYI.data():
        print("IDENT.IMPSEP.KYI are different")
        difference_count += 1

    #IDENT.IMPSEP.KYI.BASISNAME.data
    if tree1.IDENT.IMPSEP.KYI.BASISNAME.data() != tree2.IDENT.IMPSEP.KYI.BASISNAME.data():
        print("IDENT.IMPSEP.KYI.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.KYI.COMMENT.data
    if tree1.IDENT.IMPSEP.KYI.COMMENT.data() != tree2.IDENT.IMPSEP.KYI.COMMENT.data():
        print("IDENT.IMPSEP.KYI.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.NE.data
    if not (tree1.IDENT.IMPSEP.NE.data() == tree2.IDENT.IMPSEP.NE.data()).all():
        print("IDENT.IMPSEP.NE are different")
        difference_count += 1

    #IDENT.IMPSEP.NE.BASISNAME.data
    if tree1.IDENT.IMPSEP.NE.BASISNAME.data() != tree2.IDENT.IMPSEP.NE.BASISNAME.data():
        print("IDENT.IMPSEP.NE.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.NE.COMMENT.data
    if tree1.IDENT.IMPSEP.NE.COMMENT.data() != tree2.IDENT.IMPSEP.NE.COMMENT.data():
        print("IDENT.IMPSEP.NE.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.TE.data
    if not (tree1.IDENT.IMPSEP.TE.data() == tree2.IDENT.IMPSEP.TE.data()).all():
        print("IDENT.IMPSEP.TE are different")
        difference_count += 1

    #IDENT.IMPSEP.TE.BASISNAME.data
    if tree1.IDENT.IMPSEP.TE.BASISNAME.data() != tree2.IDENT.IMPSEP.TE.BASISNAME.data():
        print("IDENT.IMPSEP.TE.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.TE.COMMENT.data
    if tree1.IDENT.IMPSEP.TE.COMMENT.data() != tree2.IDENT.IMPSEP.TE.COMMENT.data():
        print("IDENT.IMPSEP.TE.COMMENT are different")
        difference_count += 1

    #IDENT.IMPSEP.TI.data
    if not (tree1.IDENT.IMPSEP.TI.data() == tree2.IDENT.IMPSEP.TI.data()).all():
        print("IDENT.IMPSEP.TI are different")
        difference_count += 1

    #IDENT.IMPSEP.TI.BASISNAME.data
    if tree1.IDENT.IMPSEP.TI.BASISNAME.data() != tree2.IDENT.IMPSEP.TI.BASISNAME.data():
        print("IDENT.IMPSEP.TI.BASISNAME are different")
        difference_count += 1

    #IDENT.IMPSEP.TI.COMMENT.data
    if tree1.IDENT.IMPSEP.TI.COMMENT.data() != tree2.IDENT.IMPSEP.TI.COMMENT.data():
        print("IDENT.IMPSEP.TI.COMMENT are different")
        difference_count += 1

    # end of IDENT.IMPSEP branch
    # --------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # store IDENT.OMPSEP branch

    #IDENT.OMPSEP.CR.data
    if tree1.IDENT.OMPSEP.CR.data() != tree2.IDENT.OMPSEP.CR.data():
        print("IDENT.OMPSEP.CR are different")
        difference_count += 1

    #IDENT.OMPSEP.CR.BASISNAME.data
    if tree1.IDENT.OMPSEP.CR.BASISNAME.data() != tree2.IDENT.OMPSEP.CR.BASISNAME.data():
        print("IDENT.OMPSEP.CR.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.CR.COMMENT.data
    if tree1.IDENT.OMPSEP.CR.COMMENT.data() != tree2.IDENT.OMPSEP.CR.COMMENT.data():
        print("IDENT.OMPSEP.CR.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.CZ.data
    if tree1.IDENT.OMPSEP.CZ.data() != tree2.IDENT.OMPSEP.CZ.data():
        print("IDENT.OMPSEP.CZ are different")
        difference_count += 1

    #IDENT.OMPSEP.CZ.BASISNAME.data
    if tree1.IDENT.OMPSEP.CZ.BASISNAME.data() != tree2.IDENT.OMPSEP.CZ.BASISNAME.data():
        print("IDENT.OMPSEP.CZ.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.CZ.COMMENT.data
    if tree1.IDENT.OMPSEP.CZ.COMMENT.data() != tree2.IDENT.OMPSEP.CZ.COMMENT.data():
        print("IDENT.OMPSEP.CZ.COMMENT are different")

    #IDENT.OMPSEP.D.data
    if not (tree1.IDENT.OMPSEP.D.data() == tree2.IDENT.OMPSEP.D.data()).all():
        print("IDENT.OMPSEP.D are different")
        difference_count += 1

    #IDENT.OMPSEP.D.BASISNAME.data
    if tree1.IDENT.OMPSEP.D.BASISNAME.data() != tree2.IDENT.OMPSEP.D.BASISNAME.data():
        print("IDENT.OMPSEP.D.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.D.COMMENT.data
    if tree1.IDENT.OMPSEP.D.COMMENT.data() != tree2.IDENT.OMPSEP.D.COMMENT.data():
        print("IDENT.OMPSEP.D.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.KYE.data
    if tree1.IDENT.OMPSEP.KYE.data() != tree2.IDENT.OMPSEP.KYE.data():
        print("IDENT.OMPSEP.KYE are different")
        difference_count += 1

    #IDENT.OMPSEP.KYE.BASISNAME.data
    if tree1.IDENT.OMPSEP.KYE.BASISNAME.data() != tree2.IDENT.OMPSEP.KYE.BASISNAME.data():
        print("IDENT.OMPSEP.KYE.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.KYE.COMMENT.data
    if tree1.IDENT.OMPSEP.KYE.COMMENT.data() != tree2.IDENT.OMPSEP.KYE.COMMENT.data():
        print("IDENT.OMPSEP.KYE.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.KYI.data
    if tree1.IDENT.OMPSEP.KYI.data() != tree2.IDENT.OMPSEP.KYI.data():
        print("IDENT.OMPSEP.KYI are different")
        difference_count += 1

    #IDENT.OMPSEP.KYI.BASISNAME.data
    if tree1.IDENT.OMPSEP.KYI.BASISNAME.data() != tree2.IDENT.OMPSEP.KYI.BASISNAME.data():
        print("IDENT.OMPSEP.KYI.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.KYI.COMMENT.data
    if tree1.IDENT.OMPSEP.KYI.COMMENT.data() != tree2.IDENT.OMPSEP.KYI.COMMENT.data():
        print("IDENT.OMPSEP.KYI.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.NE.data
    if not (tree1.IDENT.OMPSEP.NE.data() == tree2.IDENT.OMPSEP.NE.data()).all():
        print("IDENT.OMPSEP.NE are different")
        difference_count += 1

    #IDENT.OMPSEP.NE.BASISNAME.data
    if tree1.IDENT.OMPSEP.NE.BASISNAME.data() != tree2.IDENT.OMPSEP.NE.BASISNAME.data():
        print("IDENT.OMPSEP.NE.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.NE.COMMENT.data
    if tree1.IDENT.OMPSEP.NE.COMMENT.data() != tree2.IDENT.OMPSEP.NE.COMMENT.data():
        print("IDENT.OMPSEP.NE.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.TE.data
    if not (tree1.IDENT.OMPSEP.TE.data() == tree2.IDENT.OMPSEP.TE.data()).all():
        print("IDENT.OMPSEP.TE are different")
        difference_count += 1

    #IDENT.OMPSEP.TE.BASISNAME.data
    if tree1.IDENT.OMPSEP.TE.BASISNAME.data() != tree2.IDENT.OMPSEP.TE.BASISNAME.data():
        print("IDENT.OMPSEP.TE.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.TE.COMMENT.data
    if tree1.IDENT.OMPSEP.TE.COMMENT.data() != tree2.IDENT.OMPSEP.TE.COMMENT.data():
        print("IDENT.OMPSEP.TE.COMMENT are different")
        difference_count += 1

    #IDENT.OMPSEP.TI.data
    if not (tree1.IDENT.OMPSEP.TI.data() == tree2.IDENT.OMPSEP.TI.data()).all():
        print("IDENT.OMPSEP.TI are different")
        difference_count += 1

    #IDENT.OMPSEP.TI.BASISNAME.data
    if tree1.IDENT.OMPSEP.TI.BASISNAME.data() != tree2.IDENT.OMPSEP.TI.BASISNAME.data():
        print("IDENT.OMPSEP.TI.BASISNAME are different")
        difference_count += 1

    #IDENT.OMPSEP.TI.COMMENT.data
    if tree1.IDENT.OMPSEP.TI.COMMENT.data() != tree2.IDENT.OMPSEP.TI.COMMENT.data():
        print("IDENT.OMPSEP.TI.COMMENT are different")
        difference_count += 1

    # end of IDENT.OMPSEP branch
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # store IDENT branch

    #IDENT.DATE.data
    if tree1.IDENT.DATE.data() != tree2.IDENT.DATE.data():
        print("IDENT.DATE are different")
        difference_count += 1

    #IDENT.DATE.COMMENT.data
    if tree1.IDENT.DATE.COMMENT.data() != tree2.IDENT.DATE.COMMENT.data():
        print("IDENT.DATE.COMMENT are different")
        difference_count += 1

    #IDENT.DIRECTORY.data
    if tree1.IDENT.DIRECTORY.data() != tree2.IDENT.DIRECTORY.data():
        print("IDENT.DIRECTORY are different")
        difference_count += 1

    #IDENT.DIRECTORY.COMMENT.data
    if tree1.IDENT.DIRECTORY.COMMENT.data() != tree2.IDENT.DIRECTORY.COMMENT.data():
        print("IDENT.DIRECTORY.COMMENT are different")
        difference_count += 1

    #IDENT.EXP.data
    if tree1.IDENT.EXP.data() != tree2.IDENT.EXP.data():
        print("IDENT.EXP are different")
        difference_count += 1

    #IDENT.EXP.COMMENT.data
    if tree1.IDENT.EXP.COMMENT.data() != tree2.IDENT.EXP.COMMENT.data():
        print("IDENT.EXP.COMMENT are different")
        difference_count += 1

    #IDENT.GEOMETRY.data
    if tree1.IDENT.GEOMETRY.data() != tree2.IDENT.GEOMETRY.data():
        print("IDENT.GEOMETRY are different")
        difference_count += 1

    #IDENT.GEOMETRY.BASISNAME.data
    if tree1.IDENT.GEOMETRY.BASISNAME.data() != tree2.IDENT.GEOMETRY.BASISNAME.data():
        print("IDENT.GEOMETRY.BASISNAME are different")
        difference_count += 1

    #IDENT.GEOMETRY.COMMENT.data
    if tree1.IDENT.GEOMETRY.COMMENT.data() != tree2.IDENT.GEOMETRY.COMMENT.data():
        print("IDENT.GEOMETRY.COMMENT are different")
        difference_count += 1

    #IDENT.HOST.data
    if tree1.IDENT.HOST.data() != tree2.IDENT.HOST.data():
        print("IDENT.HOST are different")
        difference_count += 1

    #IDENT.HOST.COMMENT.data
    if tree1.IDENT.HOST.COMMENT.data() != tree2.IDENT.HOST.COMMENT.data():
        print("IDENT.HOST.COMMENT are different")
        difference_count += 1

    #IDENT.NS.data
    if tree1.IDENT.NS.data() != tree2.IDENT.NS.data():
        print("IDENT.NS are different")
        difference_count += 1

    #IDENT.NS.BASISNAME.data
    if tree1.IDENT.NS.BASISNAME.data() != tree2.IDENT.NS.BASISNAME.data():
        print("IDENT.NS.BASISNAME are different")
        difference_count += 1

    #IDENT.NS.COMMENT.data
    if tree1.IDENT.NS.COMMENT.data() != tree2.IDENT.NS.COMMENT.data():
        print("IDENT.NS.COMMENT are different")
        difference_count += 1

    #IDENT.NX.data
    if tree1.IDENT.NX.data() != tree2.IDENT.NX.data():
        print("IDENT.NX are different")
        difference_count += 1

    #IDENT.NX.BASISNAME.data
    if tree1.IDENT.NX.BASISNAME.data() != tree2.IDENT.NX.BASISNAME.data():
        print("IDENT.NX.BASISNAME are different")
        difference_count += 1

    #IDENT.NX.COMMENT.data
    if tree1.IDENT.NX.COMMENT.data() != tree2.IDENT.NX.COMMENT.data():
        print("IDENT.NX.COMMENT are different")
        difference_count += 1

    #IDENT.NY.data
    if tree1.IDENT.NY.data() != tree2.IDENT.NY.data():
        print("IDENT.NY are different")
        difference_count += 1

    #IDENT.NY.BASISNAME.data
    if tree1.IDENT.NY.BASISNAME.data() != tree2.IDENT.NY.BASISNAME.data():
        print("IDENT.NY.BASISNAME are different")
        difference_count += 1

    #IDENT.NY.COMMENT.data
    if tree1.IDENT.NY.COMMENT.data() != tree2.IDENT.NY.COMMENT.data():
        print("IDENT.NY.COMMENT are different")
        difference_count += 1

    #IDENT.PROBNAME.data
    if tree1.IDENT.PROBNAME.data() != tree2.IDENT.PROBNAME.data():
        print("IDENT.PROBNAME are different")
        difference_count += 1

    #IDENT.SHOT.data
    if tree1.IDENT.SHOT.data() != tree2.IDENT.SHOT.data():
        print("IDENT.SHOT are different")
        difference_count += 1

    #IDENT.SHOT.BASISNAME.data
    if tree1.IDENT.SHOT.BASISNAME.data() != tree2.IDENT.SHOT.BASISNAME.data():
        print("IDENT.SHOT.BASISNAME are different")
        difference_count += 1

    #IDENT.SHOT.COMMENT.data
    if tree1.IDENT.SHOT.COMMENT.data() != tree2.IDENT.SHOT.COMMENT.data():
        print("IDENT.SHOT.COMMENT are different")
        difference_count += 1

    #IDENT.SPECIES.data
    if tree1.IDENT.SPECIES.data() != tree2.IDENT.SPECIES.data():
        print("IDENT.SPECIES are different")
        difference_count += 1

    #IDENT.SPECIES.BASISNAME.data
    if tree1.IDENT.SPECIES.BASISNAME.data() != tree2.IDENT.SPECIES.BASISNAME.data():
        print("IDENT.SPECIES.BASISNAME are different")
        difference_count += 1

    #IDENT.SPECIES.COMMENT.data
    if tree1.IDENT.SPECIES.COMMENT.data() != tree2.IDENT.SPECIES.COMMENT.data():
        print("IDENT.SPECIES.COMMENT are different")
        difference_count += 1

    #IDENT.TIME.data
    if tree1.IDENT.TIME.data() != tree2.IDENT.TIME.data():
        print("IDENT.TIME are different")
        difference_count += 1

    #IDENT.TIME.BASISNAME.data
    if tree1.IDENT.TIME.BASISNAME.data() != tree2.IDENT.TIME.BASISNAME.data():
        print("IDENT.TIME.BASISNAME are different")
        difference_count += 1

    #IDENT.TIME.COMMENT.data
    if tree1.IDENT.TIME.COMMENT.data() != tree2.IDENT.TIME.COMMENT.data():
        print("IDENT.TIME.COMMENT are different")
        difference_count += 1

    #IDENT.UEDGEVERSION.data
    if tree1.IDENT.UEDGEVERSION.data() != tree2.IDENT.UEDGEVERSION.data():
        print("IDENT.UEDGEVERSION are different")
        difference_count += 1

    #IDENT.UEDGEVERSION.BASISNAME.data
    if tree1.IDENT.UEDGEVERSION.BASISNAME.data() != tree2.IDENT.UEDGEVERSION.BASISNAME.data():
        print("IDENT.UEDGEVERSION.BASISNAME are different")
        difference_count += 1

    #IDENT.UEDGEVERSION.COMMENT.data
    if tree1.IDENT.UEDGEVERSION.COMMENT.data() != tree2.IDENT.UEDGEVERSION.COMMENT.data():
        print("IDENT.UEDGEVERSION.COMMENT are different")
        difference_count += 1

    #IDENT.USER.data
    if tree1.IDENT.USER.data() != tree2.IDENT.USER.data():
        print("IDENT.USER are different")
        difference_count += 1

    #IDENT.USER.BASISNAME.data
    if tree1.IDENT.USER.BASISNAME.data() != tree2.IDENT.USER.BASISNAME.data():
        print("IDENT.USER.BASISNAME are different")
        difference_count += 1

    #IDENT.USER.COMMENT.data
    if tree1.IDENT.USER.COMMENT.data() != tree2.IDENT.USER.COMMENT.data():
        print("IDENT.USER.COMMENT are different")
        difference_count += 1

    # end of IDENT branch
    # ------------------------------------------------------------------------

    if difference_count == 0:
        print("The trees are same")
    else:
        print("There are " + str(difference_count) + " differences between the trees")
