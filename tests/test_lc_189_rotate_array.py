import setup_paths

from lc_189_rotate_array import RotateArray

def test_solve():

    #Test 1
    nums    = [1,2,3,4,5,6,7]
    k       = 3
    output  = [5,6,7,1,2,3,4]

    solution = RotateArray(nums, k)

    assert solution.solve() == output

    #Test 2
    nums    = [-1,-100,3,99]
    k       = 2
    output  = [3,99,-1,-100]

    solution = RotateArray(nums, k)

    assert solution.solve() == output