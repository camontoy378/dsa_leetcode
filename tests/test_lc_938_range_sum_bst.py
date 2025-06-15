import setup_paths

from lc_938_range_sum_bst import RangeSumBST

def test_solve():

    #Test 1
    input   = [10,5,15,3,7,None,18]
    low     = 7
    high    = 15

    output  = 32

    solution = RangeSumBST(input, low, high)

    assert solution.solve() == output

    #Test 2
    input   = [10,5,15,3,7,13,18,1,None,6]
    low     = 6
    high    = 10

    output  = 23

    solution = RangeSumBST(input, low, high)

    assert solution.solve() == output