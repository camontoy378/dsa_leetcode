import setup_paths

from lc_169_majority import Solution

def test_solve():

    #Test 1
    nums    = [3,2,3]
    output  = 3

    solution = Solution()

    assert solution.majorityElement(nums) == output

    #Test 2
    nums    = [2,2,1,1,1,2,2]
    output  = 2

    solution = Solution()

    assert solution.majorityElement(nums) == output