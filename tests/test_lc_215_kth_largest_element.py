import setup_paths

from lc_215_kth_largest_element import KthLargestElement

def test_heap_min_insert():

    #Test 1
    nums    = [3,2]
    k       = 2 
    output  = [2,3]

    i = 1

    solution = KthLargestElement(nums, k)
    
    solution.heap_min_insert(i, nums)

    assert solution.nums == output

    #Test 2
    nums    = [2,3,1]
    k       = 2    
    output  = [1,3,2]

    i = 2

    solution = KthLargestElement(nums, k)
    
    solution.heap_min_insert(i, nums)

    assert solution.nums == output


def test_solve():

    #Test 1
    nums    = [3,2,1,5,6,4]
    k       = 2
    output  = 5

    solution = KthLargestElement(nums, k)


    assert solution.solve() == output

    #Test 2
    nums    = [3,2,3,1,2,4,5,5,6]
    k       = 4
    output  = 4

    solution = KthLargestElement(nums, k)

    assert solution.solve() == output