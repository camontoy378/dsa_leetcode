import setup_paths

from lc_3304_kth_char import KthChar

def test_next_chars():

    #Test 1

    input   = "a"
    output  = "b"

    solution = KthChar(5)

    assert solution.next_chars(input) == output

    #Test 2

    input   = "ab"
    output  = "bc"

    solution = KthChar(5)

    assert solution.next_chars(input) == output

    #Test 3

    input   = "abbc"
    output  = "bccd"

    solution = KthChar(5)

    assert solution.next_chars(input) == output


def test_solve():

    #Test 1

    input   = 5
    output  = "b"

    solution = KthChar(input)

    assert solution.solve() == output

    #Test 2

    input   = 10
    output  = "c"

    solution = KthChar(input)

    assert solution.solve() == output