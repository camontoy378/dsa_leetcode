import setup_paths

from lc_191_num_1_bits import NumOneBits

def test_solve():

    #Test 1

    n = 11

    output = 3

    solution = NumOneBits(n)

    assert solution.solve() == output

    #Test 2

    n = 128

    output = 1

    solution = NumOneBits(n)

    assert solution.solve() == output

    #Test 3

    n = 2147483645

    output = 30

    solution = NumOneBits(n)

    assert solution.solve() == output