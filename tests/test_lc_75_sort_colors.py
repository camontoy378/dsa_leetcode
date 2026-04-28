import setup_paths

from lc_75_sort_colors import SortColors


def test_solve():

    #Test 1
    nums    = [2,0,2,1,1,0]
    output  = [0,0,1,1,2,2]

    solution = SortColors(nums)

    assert solution.solve() == output

    #Test 2
    nums    = [2,0,1]
    output  = [0,1,2]

    solution = SortColors(nums)

    assert solution.solve() == output

    #Test 3
    nums    = [0]
    output  = [0]

    solution = SortColors(nums)

    assert solution.solve() == output