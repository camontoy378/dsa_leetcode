import setup_paths

from lc_209_min_size_subarray import MinSizeSubarraySum

def test_solve():

    #Test 1
    target  = 7
    nums    = [2,3,1,2,4,3]
    output  = 2

    solution = MinSizeSubarraySum(nums, target)

    assert solution.solve() == output

    #Test 2
    target  = 4
    nums    = [1,4,4]
    output  = 1

    solution = MinSizeSubarraySum(nums, target)

    assert solution.solve() == output

    #Test 3
    target  = 11
    nums    = [1,1,1,1,1,1,1,1]
    output  = 0

    solution = MinSizeSubarraySum(nums, target)

    assert solution.solve() == output