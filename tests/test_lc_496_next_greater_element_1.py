import setup_paths
from lc_496_next_greater_element_1 import NextGreaterElement1

def test_solve():

    #Test 1
    nums1   = [4,1,2]
    nums2   = [1,3,4,2]
    output  = [-1,3,-1]

    solution = NextGreaterElement1(nums1, nums2)

    assert solution.solve() == output

    #Test 2
    nums1   = [2,4]
    nums2   = [1,2,3,4]
    output  = [3,-1]

    solution = NextGreaterElement1(nums1, nums2)

    assert solution.solve() == output