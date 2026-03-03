import setup_paths

from lc_264_ugly_num_2 import UglyNumTwo

def test_solve():

    #Test 1

    n       = 10
    output  = 12

    solution = UglyNumTwo(n)

    assert solution.solve() == output

    #Test 2

    n       = 1
    output  = 1

    solution = UglyNumTwo(n)

    assert solution.solve() == output

    #Test 3

    n       = 23
    output  = 1

    solution = UglyNumTwo(n)

    #assert solution.solve() == output