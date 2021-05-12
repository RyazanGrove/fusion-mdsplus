import MDSplus

#def compare_trees(first_tree, second_tree):
    #open first tree
#tree1 = MDSplus.Tree("uedge", -1)
    #open second treee
#tree2 = MDSplus.Tree("uedge", 170)


#print(tree1.SNAPSHOT.DIMENSIONS.IMP.data())
#print(tree2.SNAPSHOT.DIMENSIONS.IMP.data())

#print(tree1.SNAPSHOT.DIMENSIONS.IMP.COMMENT.data())
#print(tree2.SNAPSHOT.DIMENSIONS.IMP.COMMENT.data())

#print(tree1.SNAPSHOT.DIMENSIONS.IMP.BASISNAME.data())
#print(tree2.SNAPSHOT.DIMENSIONS.IMP.BASISNAME.data())


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

    if difference_count == 0:
        print("The trees are same")
    else:
        print("There are " + str(difference_number) + " differences between the trees")
