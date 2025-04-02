import setup_paths

from lc_2558_take_gifts import TakeGifts

def test_negate_array():

    #Test 1
    gifts   = [25,64,9,4,100]
    k       = 4

    output  = [-25,-64,-9,-4,-100]

    solution = TakeGifts(gifts, k)
    assert solution.negate_array(solution.gifts_array) == output


def test_solve():

    #Test 1
    gifts   = [25,64,9,4,100]
    k       = 4

    output  = 29

    solution = TakeGifts(gifts, k)
    assert solution.solve() == output

    #Test 2
    gifts   = [1,1,1,1]
    k       = 4

    output  = 4

    solution = TakeGifts(gifts, k)
    assert solution.solve() == output