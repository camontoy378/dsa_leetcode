import setup_paths

from lc_278_first_bad_ver import FirstBadVersion

def test_solve():
    
    #Test 1

    input   = 5
    bad     = 4
    output  = 4

    solution = FirstBadVersion(input, bad)

    assert solution.solve() == output


    #Test 2

    input   = 1
    bad     = 1
    output  = 1

    solution = FirstBadVersion(input, bad)

    assert solution.solve() == output