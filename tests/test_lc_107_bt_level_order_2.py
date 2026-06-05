import setup_paths

from lc_107_bt_level_order_2 import BTLevelOrderTwo

def test_solve():

    #Test 1
    root    = [3,9,20,None,None,15,7]
    output  = [[15,7],[9,20],[3]]

    solution = BTLevelOrderTwo(root)
    
    assert solution.solve() == output

    #Test 2
    root    = [1]
    output  = [[1]]

    solution = BTLevelOrderTwo(root)
    
    assert solution.solve() == output

    #Test 1
    root    = []
    output  = []

    solution = BTLevelOrderTwo(root)
    
    assert solution.solve() == output