import setup_paths

from lc_88_merge_sorted_array import MergeSortedArray

def test_solve():


    #Test 1
    nums1   = [1,2,3,0,0,0]
    m       = 3
    nums2   = [2,5,6]
    n       = 3
    output  = [1,2,2,3,5,6]

    solution = MergeSortedArray(nums1, nums2, m, n)
    
    
    assert solution.solve() == output

    #Test 2
    nums1   = [1]
    m       = 1
    nums2   = []
    n       = 0
    output  = [1]

    solution = MergeSortedArray(nums1, nums2, m, n)
    
    assert solution.solve() == output


    #Test 3
    nums1   = [0]
    m       = 0
    nums2   = [1]
    n       = 1
    output  = [1]

    solution = MergeSortedArray(nums1, nums2, m, n)
    
    assert solution.solve() == output

    #Test 4
    nums1   = [1,2,4,5,6,0]
    m       = 5
    nums2   = [3]
    n       = 1
    output  = [1,2,3,4,5,6]

    solution = MergeSortedArray(nums1, nums2, m, n)
    
    assert solution.solve() == output

    #Test5
    nums1   = [2,0]
    m       = 1
    nums2   = [1]
    n       = 1
    output  = [1,2]

    solution = MergeSortedArray(nums1, nums2, m, n)

    assert solution.solve() == output