import setup_paths

from lc_94_bt_inorder_trav import BinTreeInorderTrav

def test_solve():

    #Test 1
    input   = [1,None,2,3]

    output  = [1,3,2]

    solution = BinTreeInorderTrav()

    assert solution.solve() == True