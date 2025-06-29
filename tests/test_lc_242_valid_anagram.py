import setup_paths

from lc_242_valid_anagram import ValidAnagram

def test_solve():

    #Test 1
    s       = "anagram"
    t       = "nagaram"

    output  = True

    solution = ValidAnagram(s,t)

    assert solution.solve() == output

    #Test 2
    s       = "rat"
    t       = "car"

    output  = False

    solution = ValidAnagram(s,t)

    assert solution.solve() == output

    #Test 3
    s       = "aacc"
    t       = "ccac"

    output  = False

    solution = ValidAnagram(s,t)

    assert solution.solve() == output