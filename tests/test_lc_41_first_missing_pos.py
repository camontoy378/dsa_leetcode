import setup_paths
from lc_41_first_missing_pos import Solution

def test_firstMissingPositive():

    #Test 1
    nums    = [1,2,0]
    output  = 3

    solution = Solution()

    assert solution.firstMissingPositive(nums) == output

    #Test 2
    nums    = [3,4,-1,1]
    output  = 2

    assert solution.firstMissingPositive(nums) == output

    #Test 3
    nums    = [7,8,9,11,12]
    output  = 1

    assert solution.firstMissingPositive(nums) == output

    #Test 4
    nums    = [0,2,2,1,1]
    output  = 3

    assert solution.firstMissingPositive(nums) == output

    #Test 5
    nums    = [1,2,6,3,5,4]
    output  = 7

    assert solution.firstMissingPositive(nums) == output

    
