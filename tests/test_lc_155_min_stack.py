import setup_paths

from lc_155_min_stack import MinStack

def test_solve():

    #Test 1
    instrutcions    = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    parameters      = [[],[-2],[0],[-3],[],[],[],[]]

    output          = [None,None,None,None,-3,None,0,-2]

    solution = MinStack()

    assert solution.solve() == True