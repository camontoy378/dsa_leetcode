import setup_paths

from lc_392_is_sub_sequence import Subsequence

def test_solve():

    #Test 1
    s       = "abc" 
    t       = "ahbgdc"
    output  = True

    solution = Subsequence(s, t)

    assert solution.solve() == output


    #Test 2
    s       = "axc" 
    t       = "ahbgdc"
    output  = False

    solution = Subsequence(s, t)

    assert solution.solve() == output

    #Test 3
    s       = "" 
    t       = "ahbgdc"
    output  = True

    solution = Subsequence(s, t)

    assert solution.solve() == output

