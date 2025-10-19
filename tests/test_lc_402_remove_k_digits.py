import setup_paths

from lc_402_remove_k_digits import RemoveKDigits

def test_solve():

    #Test 1

    number  = "1432219"
    k       = 3
    output  = "1219"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output

    #Test 2

    number  = "10200"
    k       = 1
    output  = "200"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output

    #Test 3

    number  = "10"
    k       = 2
    output  = "0"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output

    #Test 4

    number  = "33526221184202197273"
    k       = 19
    output  = "0"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output

    #Test 5

    number  = "112"
    k       = 1
    output  = "11"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output

    #Test 7

    number  = "10001"
    k       = 4
    output  = "0"

    solution = RemoveKDigits(number, k)

    assert solution.solve() == output
    

