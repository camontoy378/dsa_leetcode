import setup_paths

from lc_643_max_avg_subarray import MaxAvgSubarray

def test_solve():

    #Test 1
    nums    = [1,12,-5,-6,50,3] 
    k       = 4
    output  = 12.75000

    solution = MaxAvgSubarray(nums, k)

    assert solution.solve() == output

    #Test 2
    nums    = [5]
    k       = 1
    output  = 5.00000

    solution.nums_list  = nums
    solution.k          = k

    assert solution.solve() == output

    #Test 3
    nums    = [4,2,1,3,3]
    k       = 2
    output  = 3.00000

    solution.nums_list  = nums
    solution.k          = k

    assert solution.solve() == output

