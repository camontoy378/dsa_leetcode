import setup_paths

from lc_344_reverse_string import ReverseString

def test_solve():

    #Test 1
    s       = ["h","e","l","l","o"]
    output  = ["o","l","l","e","h"]

    solution = ReverseString(s)

    solution.solve()

    assert s == output

    #Test 2
    s       = ["H","a","n","n","a","h"]
    output  = ["h","a","n","n","a","H"]

    solution = ReverseString(s)

    solution.solve()

    assert s == output