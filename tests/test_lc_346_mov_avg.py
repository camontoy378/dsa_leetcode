import setup_paths

from lc_346_mov_avg import MovingAverage

def test_solve():

    #Test 1
    input   = [3,1,10,3,5]

    solution = MovingAverage(input[0])

    assert solution.next(input[1]) == 1.0
    assert solution.next(input[2]) == 5.5
    assert solution.next(input[3]) == 4.666666666666667
    assert solution.next(input[4]) == 6.0