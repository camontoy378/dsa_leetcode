import setup_paths

from lc_27_remove_element import RemoveElement

def test_solve():

    #Test 1
    nums        = [3,2,2,3]
    val         = 3

    output      = 2
    output_nums = [2,2,3,3]

    solution = RemoveElement(nums, val)

    solve_output = solution.solve()

    assert solve_output == output
    assert solution.nums == output_nums


    #Test 2
    nums        = [0,1,2,2,3,0,4,2]
    val         = 2

    output      = 5
    output_nums = [0,1,4,0,3,2,2,2]

    solution = RemoveElement(nums, val)

    solve_output = solution.solve()

    assert solve_output == output
    assert solution.nums == output_nums