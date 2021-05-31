#
#add a command to open a tree for edit
#environment path variable must be set
#for tree mydiag use something like
#export mydiag_path=./trees\;
#
from MDSplus import Tree
from datetime import datetime
import os

# TODO: Write tree script version to master

global treeversion
treeversion = 'V{}, {}'.format('0.1', 
                datetime.now().strftime('%m/%d/%Y %H:%M:%S'))

def create_tree(name='test', path='/scratch/phys/fusion_mdsplus/trees/'):
    tree_path = '{}/{}'.format(path, name)
    os.environ[f'{name}_path'] = tree_path
    tree = Tree(tree=name,mode='NEW')

    make_diag(tree)
    make_timedep(tree)
    make_tallies(tree)
    make_snapshot(tree)
    make_movies(tree)
    make_ident(tree)

    tree.write()

def make_diag(tree):
    tree.addNode('.DIAG',usage='STRUCTURE')
    tree.addNode('.DIAG.AUG',usage='STRUCTURE')
    if True:
        tree.addNode('.DIAG.AUG.BLS_II_DPC',usage='STRUCTURE')
        if True:
            tree.addNode('.DIAG.AUG.BLS_II_DPC:AHAL_MHAL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:AHAL_MHAL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:AHAL_MHAL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:CIII_4650',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:CIII_4650:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:CIII_4650:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:CII_6581',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:CII_6581:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:CII_6581:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:COMMENT',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:COMMENT:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:COMMENT:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4340',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4340:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4340:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4861',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4861:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_4861:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_6561',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_6561:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:H0_6561:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:HALPHA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HALPHA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HALPHA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:HBETA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HBETA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HBETA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.BLS_II_DPC:HGAMMA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HGAMMA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.BLS_II_DPC:HGAMMA:COMMENT',usage='TEXT')
        tree.addNode('.DIAG.AUG.DIA',usage='STRUCTURE')
        if True:
            tree.addNode('.DIAG.AUG.DIA:AHAL_MHAL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:AHAL_MHAL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:AHAL_MHAL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:CIII_4650',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:CIII_4650:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:CIII_4650:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:CII_6581',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:CII_6581:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:CII_6581:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:COMMENT',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:COMMENT:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:COMMENT:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:H0_4340',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:H0_4340:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:H0_4340:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:H0_6561',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:H0_6561:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:H0_6561:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:HALPHA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:HALPHA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:HALPHA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:HBETA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:HBETA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:HBETA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.DIA:HGAMMA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.DIA:HGAMMA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.DIA:HGAMMA:COMMENT',usage='TEXT')
        tree.addNode('.DIAG.AUG.LAST10',usage='STRUCTURE')
        if True:
            tree.addNode('.DIAG.AUG.LAST10:AN3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:AN3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:AN3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:AN3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:AN3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:AN3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:AN3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:AN3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:AN3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:AN3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:AN3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:AN3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:COMMENT',usage='TEXT')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:COMMENT:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:COMMENT:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:DN3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:DN3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:DN3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:DN3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:DN3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:DN3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:DP3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:DP3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:DP3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:DP3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:DP3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:DP3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FC3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FC3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FC3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FC3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FC3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FC3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FE3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FE3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FE3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FE3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FE3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FE3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FI3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FI3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FI3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FI3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FI3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FI3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FL3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FL3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FL3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FL3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FL3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FL3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FN3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FN3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FN3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FN3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FN3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FN3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FO3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FO3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FO3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FO3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FO3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FO3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FT3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FT3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FT3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:FT3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:FT3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:FT3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:KE3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:KE3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:KE3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:KE3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:KE3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:KE3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:KI3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:KI3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:KI3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:KI3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:KI3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:KI3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:MN3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:MN3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:MN3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:MN3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:MN3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:MN3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:MN3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:MN3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:MN3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:MN3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:MN3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:MN3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:NE3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:NE3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:NE3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:NE3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:NE3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:NE3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:NE3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:NE3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:NE3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:NE3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:NE3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:NE3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:PO3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:PO3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:PO3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:PO3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:PO3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:PO3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:PO3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:PO3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:PO3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:PO3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:PO3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:PO3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TE3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TE3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TE3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TE3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TE3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TE3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TE3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TE3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TE3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TE3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TE3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TE3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TI3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TI3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TI3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TI3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TI3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TI3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TI3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TI3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TI3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TI3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TI3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TI3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TP3DL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TP3DL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TP3DL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:TP3DR',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:TP3DR:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:TP3DR:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VS3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VS3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VS3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VS3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VS3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VS3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VX3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VX3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VX3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VX3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VX3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VX3DI:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VY3DA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VY3DA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VY3DA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.LAST10:VY3DI',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.LAST10:VY3DI:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.LAST10:VY3DI:COMMENT',usage='TEXT')
        tree.addNode('.DIAG.AUG.Z_0_2',usage='STRUCTURE')
        if True:
            tree.addNode('.DIAG.AUG.Z_0_2:AHAL_MHAL',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:AHAL_MHAL:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:AHAL_MHAL:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:CIII_4650',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:CIII_4650:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:CIII_4650:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:CII_6581',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:CII_6581:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:CII_6581:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:COMMENT',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:COMMENT:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:COMMENT:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:H0_4340',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:H0_4340:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:H0_4340:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:H0_4861',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:H0_4861:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:H0_4861:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:H0_6561',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:H0_6561:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:H0_6561:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:HALPHA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:HALPHA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:HALPHA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:HBETA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:HBETA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:HBETA:COMMENT',usage='TEXT')
            tree.addNode('.DIAG.AUG.Z_0_2:HGAMMA',usage='SIGNAL')
            if True:
                tree.addNode('.DIAG.AUG.Z_0_2:HGAMMA:BASISNAME',usage='TEXT')
                tree.addNode('.DIAG.AUG.Z_0_2:HGAMMA:COMMENT',usage='TEXT')
        tree.addNode('.DIAG.AUG:COMMENT',usage='TEXT')
        if True:
            tree.addNode('.DIAG.AUG:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.DIAG.AUG:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.DIAG:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.DIAG:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.DIAG:COMMENT:COMMENT',usage='TEXT')

def make_ident(tree):
    tree.addNode('.IDENT',usage='STRUCTURE')
    tree.addNode('.IDENT.IMPSEP',usage='STRUCTURE')
    if True:
        tree.addNode('.IDENT.IMPSEP:COMMENT',usage='TEXT')
        if True:
            tree.addNode('.IDENT.IMPSEP:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:COMMENT:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:CR',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:CR:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:CR:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:CZ',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:CZ:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:CZ:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:D',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:D:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:D:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:KYE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:KYE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:KYE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:KYI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:KYI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:KYI:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:KYI0',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:KYI0:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:KYI0:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:NE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:NE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:NE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:TE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:TE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:TE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.IMPSEP:TI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.IMPSEP:TI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.IMPSEP:TI:COMMENT',usage='TEXT')
    tree.addNode('.IDENT.OMPSEP',usage='STRUCTURE')
    if True:
        tree.addNode('.IDENT.OMPSEP:COMMENT',usage='TEXT')
        if True:
            tree.addNode('.IDENT.OMPSEP:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:COMMENT:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:CR',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:CR:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:CR:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:CZ',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:CZ:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:CZ:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:D',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:D:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:D:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:KYE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:KYE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:KYE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:KYI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:KYI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:KYI:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:KYI0',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:KYI0:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:KYI0:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:NE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:NE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:NE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:TE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:TE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:TE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.OMPSEP:TI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.OMPSEP:TI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.OMPSEP:TI:COMMENT',usage='TEXT')
    tree.addNode('.IDENT.SEP',usage='STRUCTURE')
    if True:
        tree.addNode('.IDENT.SEP:COMMENT',usage='TEXT')
        if True:
            tree.addNode('.IDENT.SEP:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.SEP:COMMENT:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.SEP:FHE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.SEP:FHE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.SEP:FHE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.SEP:FHI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.SEP:FHI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.SEP:FHI:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.SEP:FNE',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.SEP:FNE:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.SEP:FNE:COMMENT',usage='TEXT')
        tree.addNode('.IDENT.SEP:FNI',usage='SIGNAL')
        if True:
            tree.addNode('.IDENT.SEP:FNI:BASISNAME',usage='TEXT')
            tree.addNode('.IDENT.SEP:FNI:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:B0',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:B0:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:B0:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:B2FGMTRYID',usage='TEXT')
    if True:
        tree.addNode('.IDENT:B2FGMTRYID:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:B2FGMTRYID:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:B2FPLASMAID',usage='TEXT')
    if True:
        tree.addNode('.IDENT:B2FPLASMAID:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:B2FPLASMAID:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:B2FSTATEID',usage='TEXT')
    if True:
        tree.addNode('.IDENT:B2FSTATEID:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:B2FSTATEID:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:B2FSTATIID',usage='TEXT')
    if True:
        tree.addNode('.IDENT:B2FSTATIID:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:B2FSTATIID:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.IDENT:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:COMMENTS',usage='TEXT')
    if True:
        tree.addNode('.IDENT:COMMENTS:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:COMMENTS:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:DATE',usage='TEXT')
    if True:
        tree.addNode('.IDENT:DATE:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:DATE:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:DIRECTORY',usage='TEXT')
    if True:
        tree.addNode('.IDENT:DIRECTORY:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:DIRECTORY:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:DRIFTON',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:DRIFTON:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:DRIFTON:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:EXP',usage='TEXT')
    if True:
        tree.addNode('.IDENT:EXP:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:EXP:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:GEOMETRY',usage='TEXT')
    if True:
        tree.addNode('.IDENT:GEOMETRY:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:GEOMETRY:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:HOST',usage='TEXT')
    if True:
        tree.addNode('.IDENT:HOST:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:HOST:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:MAIN',usage='TEXT')
    if True:
        tree.addNode('.IDENT:MAIN:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:MAIN:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:NS',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:NS:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:NS:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:NX',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:NX:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:NX:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:NY',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:NY:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:NY:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:OBJECTCODE',usage='TEXT')
    if True:
        tree.addNode('.IDENT:OBJECTCODE:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:OBJECTCODE:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:PHYSICS',usage='TEXT')
    if True:
        tree.addNode('.IDENT:PHYSICS:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:PHYSICS:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:PROBNAME',usage='TEXT')
    if True:
        tree.addNode('.IDENT:PROBNAME:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:PROBNAME:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:SHOT',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:SHOT:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:SHOT:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:SPECIES',usage='TEXT')
    if True:
        tree.addNode('.IDENT:SPECIES:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:SPECIES:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:TIME',usage='NUMERIC')
    if True:
        tree.addNode('.IDENT:TIME:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:TIME:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:UEDGETOP',usage='TEXT')
    if True:
        tree.addNode('.IDENT:UEDGETOP:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:UEDGETOP:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:UEDGEVERSION',usage='TEXT')
    if True:
        tree.addNode('.IDENT:UEDGEVERSION:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:UEDGEVERSION:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:USER',usage='TEXT')
    if True:
        tree.addNode('.IDENT:USER:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:USER:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:VERSION',usage='TEXT')
    if True:
        tree.addNode('.IDENT:VERSION:BASISNAME',usage='TEXT')
        tree.addNode('.IDENT:VERSION:COMMENT',usage='TEXT')
    tree.addNode('.IDENT:TREEVERSION',usage='TEXT')
    if True:
        tree.addNode('.IDENT:TREEVERSION:COMMENT',usage='TEXT')
        tree.IDENT.TREEVERSION.putData(treeversion)
        tree.IDENT.TREEVERSION.COMMENT.putData('Version number and date of creation of the UEDGE tree')

def make_movies(tree):
    tree.addNode('.MOVIES',usage='STRUCTURE')
    tree.addNode('.MOVIES:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.MOVIES:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:DAB2',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:DAB2:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:DAB2:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:DMB2',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:DMB2:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:DMB2:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:NA',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:NA:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:NA:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:NE',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:NE:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:NE:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:RQAHESUM',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:RQAHESUM:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:RQAHESUM:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:TE',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:TE:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:TE:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:TI',usage='SIGNAL')
    if True:
        tree.addNode('.MOVIES:TI:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:TI:COMMENT',usage='TEXT')
    tree.addNode('.MOVIES:TIME',usage='NUMERIC')
    if True:
        tree.addNode('.MOVIES:TIME:BASISNAME',usage='TEXT')
        tree.addNode('.MOVIES:TIME:COMMENT',usage='TEXT')

def make_snapshot(tree):
    tree.addNode('.SNAPSHOT',usage='STRUCTURE')
    tree.addNode('.SNAPSHOT.DIMENSIONS',usage='STRUCTURE')
    if True:
        tree.addNode('.SNAPSHOT.DIMENSIONS:COMMENT',usage='TEXT')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:COMMENT:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:IMP',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:IMP:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:IMP:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NATM',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NATM:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NATM:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NION',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NION:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NION:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NMOL',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NMOL:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NMOL:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NS',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NS:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NS:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:NY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:NY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:NY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:OMP',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:OMP:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:OMP:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:SEP',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:SEP:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:SEP:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:TARG1',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG1:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG1:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:TARG2',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG2:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG2:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:TARG3',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG3:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG3:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.DIMENSIONS:TARG4',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG4:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.DIMENSIONS:TARG4:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT.GRID',usage='STRUCTURE')
    if True:
        tree.addNode('.SNAPSHOT.GRID:AM',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:AM:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:AM:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:BOTTOMIX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:BOTTOMIX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:BOTTOMIX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:BOTTOMIY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:BOTTOMIY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:BOTTOMIY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:COMMENT',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:COMMENT:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:COMMENT:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CR',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CR:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CR:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CR_X',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CR_X:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CR_X:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CR_Y',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CR_Y:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CR_Y:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CZ',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CZ:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CZ:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CZ_X',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CZ_X:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CZ_X:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:CZ_Y',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:CZ_Y:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:CZ_Y:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSPAR',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSPAR:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSPAR:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSPOL',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSPOL:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSPOL:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSRAD',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSRAD:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSRAD:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSTARG1',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSTARG1:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSTARG1:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSTARG2',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSTARG2:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSTARG2:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSTARG3',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSTARG3:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSTARG3:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:DSTARG4',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:DSTARG4:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:DSTARG4:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:LEFTIX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:LEFTIX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:LEFTIX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:LEFTIY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:LEFTIY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:LEFTIY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:POT',usage='SIGNAL')
        if True:
            tree.addNode('.SNAPSHOT.GRID:POT:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:POT:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:POTI',usage='SIGNAL')
        if True:
            tree.addNode('.SNAPSHOT.GRID:POTI:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:POTI:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:PSIN',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:PSIN:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:PSIN:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:PSINRAD',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:PSINRAD:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:PSINRAD:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:R',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:R:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:R:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:REGFLX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:REGFLX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:REGFLX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:REGFLY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:REGFLY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:REGFLY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:REGVOL',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:REGVOL:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:REGVOL:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:RIGHTIX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:RIGHTIX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:RIGHTIX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:RIGHTIY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:RIGHTIY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:RIGHTIY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:TOPIX',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:TOPIX:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:TOPIX:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:TOPIY',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:TOPIY:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:TOPIY:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:VESSEL',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:VESSEL:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:VESSEL:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:Z',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:Z:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:Z:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:ZA',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:ZA:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:ZA:COMMENT',usage='TEXT')
        tree.addNode('.SNAPSHOT.GRID:ZN',usage='NUMERIC')
        if True:
            tree.addNode('.SNAPSHOT.GRID:ZN:BASISNAME',usage='TEXT')
            tree.addNode('.SNAPSHOT.GRID:ZN:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:ALF',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:ALF:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:ALF:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:B',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:B:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:B:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:D',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:D:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:D:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:DAB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:DAB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:DAB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:DIB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:DIB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:DIB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:DMB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:DMB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:DMB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:DP',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:DP:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:DP:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FCHX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FCHX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FCHX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FCHY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FCHY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FCHY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHEX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHEX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHEX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHEY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHEY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHEY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHIX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHIX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHIX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHIY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHIY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHIY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHMX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHMX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHMX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHMY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHMY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHMY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHPX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHPX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHPX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHPY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHPY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHPY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHTX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHTX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHTX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FHTY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FHTY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FHTY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FMOX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FMOX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FMOX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FMOY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FMOY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FMOY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAX_32',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAX_32:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAX_32:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAX_52',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAX_52:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAX_52:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAY_32',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAY_32:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAY_32:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:FNAY_52',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:FNAY_52:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:FNAY_52:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:HX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:HX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:HX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:HY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:HY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:HY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:HY1',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:HY1:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:HY1:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:KYE',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:KYE:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:KYE:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:KYI',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:KYI:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:KYI:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:KYI0',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:KYI0:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:KYI0:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:NA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:NA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:NA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:NE',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:NE:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:NE:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PEFA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PEFA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PEFA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PEFM',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PEFM:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PEFM:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PFLA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PFLA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PFLA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PFLM',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PFLM:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PFLM:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PO',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PO:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PO:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:PR',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:PR:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:PR:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RCXHI',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RCXHI:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RCXHI:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RCXMO',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RCXMO:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RCXMO:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RCXNA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RCXNA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RCXNA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:REFA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:REFA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:REFA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:REFM',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:REFM:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:REFM:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RFLA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RFLA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RFLA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RFLM',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RFLM:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RFLM:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RQAHE',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RQAHE:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RQAHE:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RQBRM',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RQBRM:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RQBRM:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RQRAD',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RQRAD:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RQRAD:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RRAHI',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RRAHI:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RRAHI:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RRAMO',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RRAMO:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RRAMO:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RRANA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RRANA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RRANA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RSAHI',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RSAHI:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RSAHI:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RSAMO',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RSAMO:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RSAMO:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:RSANA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:RSANA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:RSANA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:SIG',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:SIG:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:SIG:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:SX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:SX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:SX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:SY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:SY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:SY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TAB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:TAB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TAB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TE',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:TE:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TE:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TEXTAN',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:TEXTAN:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TEXTAN:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TEXTCOMP',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:TEXTCOMP:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TEXTCOMP:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TEXTIN',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:TEXTIN:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TEXTIN:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TEXTMN',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:TEXTMN:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TEXTMN:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TEXTPL',usage='TEXT')
    if True:
        tree.addNode('.SNAPSHOT:TEXTPL:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TEXTPL:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TI',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:TI:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TI:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TIB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:TIB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TIB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:TMB2',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:TMB2:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:TMB2:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:UA',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:UA:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:UA:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:VISC',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:VISC:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:VISC:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:VLAX',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:VLAX:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:VLAX:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:VLAY',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:VLAY:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:VLAY:COMMENT',usage='TEXT')
    tree.addNode('.SNAPSHOT:VOL',usage='SIGNAL')
    if True:
        tree.addNode('.SNAPSHOT:VOL:BASISNAME',usage='TEXT')
        tree.addNode('.SNAPSHOT:VOL:COMMENT',usage='TEXT')

def make_tallies(tree):
    tree.addNode('.TALLIES',usage='STRUCTURE')
    tree.addNode('.TALLIES:B2DIVUA',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2DIVUA:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2DIVUA:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2DIVUE',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2DIVUE:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2DIVUE:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2EXBA',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2EXBA:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2EXBA:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2EXBE',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2EXBE:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2EXBE:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2FRAA',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2FRAA:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2FRAA:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2JOULE',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2JOULE:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2JOULE:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2QIE',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2QIE:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2QIE:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2SHE',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2SHE:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2SHE:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2SHE0',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2SHE0:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2SHE0:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2SHI',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2SHI:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2SHI:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2SHI0',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2SHI0:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2SHI0:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBCSCHREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBCSCHREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBCSCHREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBCSHEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBCSHEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBCSHEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBCSHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBCSHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBCSHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBCSMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBCSMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBCSMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBCSNAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBCSNAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBCSNAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBRSCHREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBRSCHREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBRSCHREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBRSHEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBRSHEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBRSHEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBRSHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBRSHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBRSHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBRSMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBRSMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBRSMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STBRSNAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STBRSNAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STBRSNAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2STR',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2STR:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2STR:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2VISA',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2VISA:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2VISA:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2WRONG1',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2WRONG1:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2WRONG1:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2WRONG2',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2WRONG2:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2WRONG2:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:B2WRONG3',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:B2WRONG3:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:B2WRONG3:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.TALLIES:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FCHXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FCHXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FCHXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FCHYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FCHYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FCHYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHEXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHEXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHEXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHEYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHEYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHEYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHIXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHIXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHIXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHIYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHIYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHIYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHMXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHMXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHMXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHMYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHMYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHMYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHPXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHPXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHPXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHPYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHPYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHPYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHTXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHTXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHTXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FHTYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FHTYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FHTYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FNAXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FNAXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FNAXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:FNAYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:FNAYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:FNAYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:NAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:NAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:NAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:NE2REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:NE2REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:NE2REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:NEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:NEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:NEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:NIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:NIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:NIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:NS',usage='TEXT')
    if True:
        tree.addNode('.TALLIES:NS:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:NS:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:POREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:POREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:POREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:QCONVEXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:QCONVEXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:QCONVEXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:QCONVEYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:QCONVEYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:QCONVEYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:QCONVIXREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:QCONVIXREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:QCONVIXREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:QCONVIYREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:QCONVIYREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:QCONVIYREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RCXHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RCXHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RCXHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RCXMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RCXMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RCXMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RCXNAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RCXNAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RCXNAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESCOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESCOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESCOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESCO_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESCO_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESCO_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESHEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESHEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESHEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESHE_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESHE_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESHE_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESHI_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESHI_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESHI_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESMO_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESMO_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESMO_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESMTREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESMTREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESMTREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESMT_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESMT_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESMT_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESPOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESPOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESPOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RESPO_REG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RESPO_REG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RESPO_REG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RQAHEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RQAHEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RQAHEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RRAHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RRAHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RRAHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RRAMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RRAMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RRAMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RRANAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RRANAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RRANAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RSAHIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RSAHIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RSAHIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RSAMOREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RSAMOREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RSAMOREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:RSANAREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:RSANAREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:RSANAREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:TEREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:TEREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:TEREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:TIME',usage='NUMERIC')
    if True:
        tree.addNode('.TALLIES:TIME:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:TIME:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:TIREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:TIREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:TIREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:VOLREG',usage='SIGNAL')
    if True:
        tree.addNode('.TALLIES:VOLREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:VOLREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:VREG',usage='TEXT')
    if True:
        tree.addNode('.TALLIES:VREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:VREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:XREG',usage='TEXT')
    if True:
        tree.addNode('.TALLIES:XREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:XREG:COMMENT',usage='TEXT')
    tree.addNode('.TALLIES:YREG',usage='TEXT')
    if True:
        tree.addNode('.TALLIES:YREG:BASISNAME',usage='TEXT')
        tree.addNode('.TALLIES:YREG:COMMENT',usage='TEXT')

def make_timedep(tree):
    tree.addNode('.TIMEDEP',usage='STRUCTURE')
    tree.addNode('.TIMEDEP:COMMENT',usage='TEXT')
    if True:
        tree.addNode('.TIMEDEP:COMMENT:BASISNAME',usage='TEXT')
        tree.addNode('.TIMEDEP:COMMENT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:DN',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:DN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:DN:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:DN:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:DN:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:DN:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:DN:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:DN:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:DP',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:DP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:DP:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:DP:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:DP:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:DP:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:DP:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:DP:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:FCH',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:FCH:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:DIVINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:DIVINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:DIVINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:MCWINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:MCWINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:MCWINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:TARG1INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:TARG1INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:TARG1INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:TARG2INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:TARG2INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:TARG2INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:TARG3INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:TARG3INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:TARG3INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FCH:TARG4INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FCH:TARG4INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FCH:TARG4INT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:FEE',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:FEE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:DIVINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:DIVINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:DIVINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:MCWINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:MCWINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:MCWINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:TARG1INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:TARG1INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:TARG1INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:TARG2INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:TARG2INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:TARG2INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:TARG3INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:TARG3INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:TARG3INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEE:TARG4INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEE:TARG4INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEE:TARG4INT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:FEI',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:FEI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:DIVINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:DIVINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:DIVINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:MCWINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:MCWINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:MCWINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:TARG1INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:TARG1INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:TARG1INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:TARG2INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:TARG2INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:TARG2INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:TARG3INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:TARG3INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:TARG3INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FEI:TARG4INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FEI:TARG4INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FEI:TARG4INT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:FET',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:FET:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:DIVINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:DIVINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:DIVINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:MCWINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:MCWINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:MCWINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:TARG1INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:TARG1INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:TARG1INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:TARG2INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:TARG2INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:TARG2INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:TARG3INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:TARG3INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:TARG3INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FET:TARG4INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FET:TARG4INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FET:TARG4INT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:FNI',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:FNI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:DIVINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:DIVINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:DIVINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:MCWINT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:MCWINT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:MCWINT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:TARG1INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:TARG1INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:TARG1INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:TARG2INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:TARG2INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:TARG2INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:TARG3INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:TARG3INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:TARG3INT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:FNI:TARG4INT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:FNI:TARG4INT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:FNI:TARG4INT:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:HALCORE',usage='SIGNAL')
    if True:
        tree.addNode('.TIMEDEP:HALCORE:BASISNAME',usage='TEXT')
        tree.addNode('.TIMEDEP:HALCORE:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:HALDIV',usage='SIGNAL')
    if True:
        tree.addNode('.TIMEDEP:HALDIV:BASISNAME',usage='TEXT')
        tree.addNode('.TIMEDEP:HALDIV:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:HALSOL',usage='SIGNAL')
    if True:
        tree.addNode('.TIMEDEP:HALSOL:BASISNAME',usage='TEXT')
        tree.addNode('.TIMEDEP:HALSOL:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:IMP',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:IMP:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:DN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:DN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:DN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:DP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:DP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:DP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:DS',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:IMP:DS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:DS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:KE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:KE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:KE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:KI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:KI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:KI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:TI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:VS',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:VS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:VS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:VX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:VX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:VX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:IMP:VY',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:IMP:VY:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:IMP:VY:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:KE',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:KE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:KE:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:KE:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:KE:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:KE:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:KE:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:KE:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:KI',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:KI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:KI:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:KI:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:KI:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:KI:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:KI:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:KI:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:NE',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:OMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:PWDENMAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:PWDENMAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:PWDENMAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG1MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG1MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG1MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG1SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG1SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG1SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG2MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG2MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG2MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG2SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG2SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG2SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG3MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG3MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG3MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG3SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG3SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG3SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG4MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG4MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG4MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:NE:TARG4SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:NE:TARG4SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:NE:TARG4SEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:OMP',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:OMP:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:DN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:DN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:DN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:DP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:DP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:DP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:DS',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:OMP:DS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:DS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:KE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:KE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:KE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:KI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:KI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:KI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:TI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:VS',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:VS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:VS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:VX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:VX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:VX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:OMP:VY',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:OMP:VY:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:OMP:VY:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:PO',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:OMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:PWDENMAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:PWDENMAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:PWDENMAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG1MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG1MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG1MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG1SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG1SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG1SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG2MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG2MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG2MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG2SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG2SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG2SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG3MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG3MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG3MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG3SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG3SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG3SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG4MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG4MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG4MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:PO:TARG4SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:PO:TARG4SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:PO:TARG4SEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TARGET1',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TARGET1:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:DA',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:DA:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:DA:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:DS',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:DS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:DS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FC',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FC:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FC:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FL',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FL:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FL:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:FT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:FT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:FT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET1:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET1:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET1:TI:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TARGET2',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TARGET2:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:DA',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:DA:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:DA:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:DS',usage='NUMERIC')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:DS:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:DS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FC',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FC:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FC:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FL',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FL:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FL:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:FT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:FT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:FT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET2:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET2:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET2:TI:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TARGET3',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TARGET3:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FC',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FC:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FC:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FL',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FL:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FL:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:FT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:FT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:FT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET3:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET3:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET3:TI:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TARGET4',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TARGET4:AN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:AN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:AN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FC',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FC:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FC:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FL',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FL:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FL:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:FT',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:FT:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:FT:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:MN',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:MN:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:MN:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:NE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:NE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:NE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:PO',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:PO:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:PO:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:TE',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:TE:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TARGET4:TI',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TARGET4:TI:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TARGET4:TI:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TE',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TE:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:OMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:PWDENMAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:PWDENMAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:PWDENMAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG1MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG1MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG1MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG1SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG1SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG1SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG2MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG2MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG2MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG2SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG2SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG2SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG3MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG3MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG3MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG3SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG3SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG3SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG4MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG4MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG4MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TE:TARG4SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TE:TARG4SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TE:TARG4SEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TI',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:TI:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:OMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:PWDENMAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:PWDENMAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:PWDENMAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG1MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG1MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG1MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG1SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG1SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG1SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG2MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG2MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG2MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG2SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG2SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG2SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG3MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG3MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG3MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG3SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG3SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG3SEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG4MAX',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG4MAX:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG4MAX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:TI:TARG4SEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:TI:TARG4SEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:TI:TARG4SEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:TIME',usage='NUMERIC')
    if True:
        tree.addNode('.TIMEDEP:TIME:BASISNAME',usage='TEXT')
        tree.addNode('.TIMEDEP:TIME:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:VS',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:VS:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VS:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VS:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VS:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VS:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VS:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VS:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:VX',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:VX:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VX:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VX:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VX:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VX:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VX:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VX:OMPSEP:COMMENT',usage='TEXT')
    tree.addNode('.TIMEDEP:VY',usage='STRUCTURE')
    if True:
        tree.addNode('.TIMEDEP:VY:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VY:IMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VY:IMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VY:IMPSEP:COMMENT',usage='TEXT')
        tree.addNode('.TIMEDEP:VY:OMPSEP',usage='SIGNAL')
        if True:
            tree.addNode('.TIMEDEP:VY:OMPSEP:BASISNAME',usage='TEXT')
            tree.addNode('.TIMEDEP:VY:OMPSEP:COMMENT',usage='TEXT')


