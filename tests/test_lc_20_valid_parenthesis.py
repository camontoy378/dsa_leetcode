import pytest
import setup_paths

from lc_20_valid_parenthesis import ValidParenthesis

#@pytest.mark.skip(reason="Cuz")
def test_solve():

    
    #Test 1
    input = "()"

    solution = ValidParenthesis(input)
    
    assert solution.solve() == True

    #Test 2
    solution.input = "()[]{}"

    assert solution.solve() == True

    #Test 3
    solution.input = "(]"

    assert solution.solve() == False

    #Test 4
    solution.input = "()[]{}"

    assert solution.solve() == True
    
    #Test 5
    solution.input = "([)]"

    assert solution.solve() == False