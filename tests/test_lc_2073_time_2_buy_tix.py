import setup_paths

from lc_2073_time_2_buy_tix import TimeToBuyTix

def test_solve():

    #Test 1

    tickets = [2,3,2]
    k       = 2
    output  = 6

    solution = TimeToBuyTix()

    #assert solution.solve(tickets, k) == output


    #Test 2

    tickets = [5,1,1,1]
    k       = 0
    output  = 8

    solution = TimeToBuyTix()

    #assert solution.solve(tickets, k) == output


    #Test 3

    tickets = [84,49,5,24,70,77,87,8]
    k       = 3
    output  = 154

    solution = TimeToBuyTix()

    assert solution.solve(tickets, k) == output
