import setup_paths

from lc_1346_check_n_double_exists import CheckNDoubleExists

def test_solve():

    #Test 1
    input   = [10,2,5,3]
    output  = True

    solution = CheckNDoubleExists(input)

    assert solution.solve() == output

    #Test 2
    input   = [3,1,7,11]
    output  = False

    solution.int_array = input

    assert solution.solve() == output