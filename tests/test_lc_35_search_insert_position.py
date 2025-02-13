import setup_paths

from lc_35_search_insert_position import SearchInsertPosition

def test_solve():

    #Test 1
    input   = [1,3,5,6]
    target  = 5
    output  = 2

    solution = SearchInsertPosition(input, target)

    assert solution.solve() == output

    #Test 2
    input   = [1,3,5,6]
    target  = 2
    output  = 1

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

    #Test 3
    input   = [1,3,5,6]
    target  = 7
    output  = 4

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

    #Test 4
    input   = [1,3,5,6]
    target  = 0
    output  = 0

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

    #Test 5
    input   = [1]
    target  = 1
    output  = 0

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

    #Test 6
    input   = [1001]
    target  = 5
    output  = 0

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

    #Test 7
    input   = [1,3]
    target  = 0
    output  = 0

    solution.nums_list  = input
    solution.target_num = target

    assert solution.solve() == output

