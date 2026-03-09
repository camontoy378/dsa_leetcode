import setup_paths

from lc_1387_sort_by_power import SortByPower

def test_get_integer_power():

    #Test 1
    lo      = 12
    hi      = 15
    k       = 2
    output  = 13

    steps_dict  = {}

    solution = SortByPower(lo, hi, k)

    assert solution.get_integer_power(steps_dict, 3) == 7

    #Test 2
    assert solution.get_integer_power(steps_dict, 12) == 9

    #Test 3
    assert solution.get_integer_power(steps_dict, 15) == 17

    #Test 4
    assert solution.get_integer_power(steps_dict, 9) == 19



def test_solve():

    #Test 1
    lo      = 12
    hi      = 15
    k       = 2
    output  = 13

    solution = SortByPower(lo, hi, k)

    assert solution.solve() == output

    #Test 2
    lo      = 7
    hi      = 11
    k       = 4
    output  = 7

    solution = SortByPower(lo, hi, k)

    assert solution.solve() == output