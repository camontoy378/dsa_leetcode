import setup_paths

from lc_1_two_sum import TwoSum

def test_solve():

    #Test 1
    nums    = [2,7,11,15]
    target  = 9
    output  = [0,1]

    solution = TwoSum()

    assert ( solution.twoSum(nums, target) == output)

    #Test 2
    nums    = [3,2,4]
    target  = 6
    output  = [1,2]

    assert ( solution.twoSum(nums, target) == output)

    #Test 3
    nums    = [3,3]
    target  = 6
    output  = [0,1]

    assert ( solution.twoSum(nums, target) == output)