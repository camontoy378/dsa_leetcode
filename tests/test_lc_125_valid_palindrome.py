import setup_paths

from lc_125_valid_palindrome import ValidPalindrome

def test_solve():

    #Test 1
    s       = "A man, a plan, a canal: Panama"
    output  = True

    solution = ValidPalindrome(s)

    assert solution.solve() == output

    #Test 2
    s       = "race a car"
    output  = False

    solution = ValidPalindrome(s)

    assert solution.solve() == output

    #Test 3
    s       = " "
    output  = True

    solution = ValidPalindrome(s)

    assert solution.solve() == output