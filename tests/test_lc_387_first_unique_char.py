import setup_paths

from lc_387_first_unique_char import FirstUniqueChar

def test_solve():

    #Test 1

    s       = "leetcode"
    output  = 0

    solution = FirstUniqueChar(s)

    assert solution.solve() == output

    #Test 2

    s       = "loveleetcode"
    output  = 2

    solution = FirstUniqueChar(s)

    assert solution.solve() == output

    #Test 3

    s       = "aabb"
    output  = -1

    solution = FirstUniqueChar(s)

    assert solution.solve() == output