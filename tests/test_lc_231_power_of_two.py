import setup_paths

from lc_231_power_of_two import PowerOfTwo

def test_solve():

    #Test 1
    input   = 1
    output  = True

    solution = PowerOfTwo(input)

    assert solution.solve() == output

    #Test 2
    input   = 16
    output  = True

    solution = PowerOfTwo(input)

    assert solution.solve() == output

    #Test 3
    input   = 3
    output  = False

    solution = PowerOfTwo(input)

    assert solution.solve() == output

