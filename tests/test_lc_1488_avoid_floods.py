import setup_paths

from lc_1488_avoid_floods import AvoidFloods

def test_pop_index_of_num_greater_than():

    #Test 1
    rains   = [1,2,0,0,2,1]
    dry_arr = [2,3]
    number  = 1

    output  = 2
    
    solution = AvoidFloods(rains)

    assert solution.pop_index_of_next_available_dry_day(dry_arr, number) == output

    #Test 2
    rains   = [1,2,0,0,2,1]
    dry_arr = [2,3]
    number  = 4

    output  = 0
    
    solution = AvoidFloods(rains)

    assert solution.pop_index_of_next_available_dry_day(dry_arr, number) == output


def test_solve():
    
    #Test 1

    rains   = [1,2,3,4]
    output  = [-1,-1,-1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 2

    rains   = [1,2,0,0,2,1]
    output  = [-1,-1,2,1,-1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 3

    rains   = [1,2,0,1,2]
    output  = []

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 4

    rains   = [69,0,0,0,69]
    output  = [-1,69,1,1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 5

    rains   = [1,2,0,2,3,0,1]
    output  = [-1,-1,2,-1,-1,1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 6

    rains   = [0,1,1]
    output  = []

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 7

    rains   = [1,0,2,0,2,1]
    output  = [-1,1,-1,2,-1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 8

    rains       = [1,0,2,0,3,0,2,0,0,0,1,2,3]
    output      = [-1,1,-1,2,-1,3,-1,2,1,1,-1,-1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output

    #Test 9

    rains       = [3,0,0,1,2,0,0,1,3,2]
    output      = [-1,3,1,-1,-1,1,2,-1,-1,-1]

    solution = AvoidFloods(rains)

    assert solution.solve() == output