import setup_paths

from lc_217_contains_duplicate import ContainsDuplicate

def test_solve():

    #Test 1
    input   = [1,2,3,1]
    output  = True

    solution = ContainsDuplicate(input)

    assert solution.solve() == output

    #Test 2
    input   = [1,2,3,4]
    output  = False

    solution = ContainsDuplicate(input)

    assert solution.solve() == output

    #Test 3
    input   = [1,1,1,3,3,4,3,2,4,2]
    output  = True

    solution = ContainsDuplicate(input)

    assert solution.solve() == output