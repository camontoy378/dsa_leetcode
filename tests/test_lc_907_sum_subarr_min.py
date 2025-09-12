import setup_paths

from lc_907_sum_subarr_min import SumSubarrayMinimuns

def test_solve():

    #Test 1
    input   = [3,1,2,4]
    output  = 17

    solution = SumSubarrayMinimuns(input)

    assert solution.solve() == output

    #Test 2
    input   = [11,81,94,43,3]
    output  = 444

    solution = SumSubarrayMinimuns(input)

    assert solution.solve() == output