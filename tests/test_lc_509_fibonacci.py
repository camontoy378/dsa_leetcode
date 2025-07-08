import setup_paths

from lc_509_fibonacci import FibonacciNumber

def test_solve():

    #Test 1

    input   = 2
    output  = 1

    solution = FibonacciNumber(input)

    assert solution.solve() == output


    #Test 2

    input   = 3
    output  = 2

    solution = FibonacciNumber(input)

    assert solution.solve() == output

    #Test 3

    input   = 4
    output  = 3

    solution = FibonacciNumber(input)

    assert solution.solve() == output