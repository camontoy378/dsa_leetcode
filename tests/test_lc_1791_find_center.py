import setup_paths

from lc_1791_find_center import FindCenter

def test_solve():

    #Test 1
    input   = [[1,2],[2,3],[4,2]]
    output  = 2

    solution = FindCenter(input)

    assert solution.solve() == output

    #Test 2
    input   = [[1,2],[5,1],[1,3],[1,4]]
    output  = 1

    solution = FindCenter(input)

    assert solution.solve() == output