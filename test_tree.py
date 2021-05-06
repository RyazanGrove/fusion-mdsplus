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




    if difference_count == 0:
        print("The trees are same")
    else:
        print("There are " + str(difference_number) + " differences between the trees")
