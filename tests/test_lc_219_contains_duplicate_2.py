import setup_paths

from lc_219_contains_duplicate_2 import ContainsDuplicate

def test_solve():

    #Test 1
    nums    = [1,2,3,1]
    k       = 3
    output  = True


    solution = ContainsDuplicate(nums, k)

    assert solution.solve() == output

    #Test 2
    nums    = [1,0,1,1]
    k       = 1
    output  = True


    solution = ContainsDuplicate(nums, k)

    assert solution.solve() == output

    #Test 3
    nums    = [1,2,3,1,2,3]
    k       = 2
    output  = False


    solution = ContainsDuplicate(nums, k)

    assert solution.solve() == output

    #Test 4
    nums    = [99,99]
    k       = 2
    output  = True


    solution = ContainsDuplicate(nums, k)

    assert solution.solve() == output

    