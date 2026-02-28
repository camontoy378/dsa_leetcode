import setup_paths

from lc_111_min_depth_bt import MinDepthBT


def test_solve():

    #Test 1
    root    = [3,9,20,None,None,15,7]
    output  = 2

    solution = MinDepthBT(root)

    #assert solution.solve() == True