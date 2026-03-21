import setup_paths

from lc_136_single_number import SingleNumber

def test_solve():

    #Test 1
    nums    = [2,2,1]
    output  = 1

    solution = SingleNumber(nums)

    assert solution.solve() == output

    #Test 2
    nums    = [4,1,2,1,2]
    output  = 4

    solution = SingleNumber(nums)

    assert solution.solve() == output

    #Test 3
    nums    = [1]
    output  = 1

    solution = SingleNumber(nums)

    assert solution.solve() == output