import setup_paths

from lc_70_climbing_stairs import ClimbingStairs

def test_solve():

    #Test 1
    input = 1
    output = 1

    solution = ClimbingStairs(input)

    assert solution.solve() == output

    #Test 2
    input = 2
    output = 2

    solution = ClimbingStairs(input)

    assert solution.solve() == output

    #Test 3
    input = 3
    output = 3

    solution = ClimbingStairs(input)

    assert solution.solve() == output

    #Test 4
    input = 4
    output = 5

    solution = ClimbingStairs(input)

    assert solution.solve() == output

    #Test 5
    input = 5
    output = 8

    solution = ClimbingStairs(input)

    assert solution.solve() == output

