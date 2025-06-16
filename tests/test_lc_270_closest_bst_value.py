import setup_paths

from lc_270_closest_bst_value import ClosestBSTValue

def test_solve():

    #Test 1
    input   = [4,2,5,1,3]
    target  = 3.714286
    output  = 4

    solution = ClosestBSTValue(input, target)

    assert solution.solve() == output

    #Test 2
    input   = [1]
    target  = 4.428571
    output  = 1

    solution = ClosestBSTValue(input, target)

    assert solution.solve() == output