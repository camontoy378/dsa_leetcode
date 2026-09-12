import setup_paths

from lc_322_coin_change import CoinChange

def test_solve():

    #Test 1
    coins   = [1,2,5]
    amount  = 11
    output  = 3

    solution = CoinChange(coins, amount)

    assert solution.solve() == output


    #Test 2
    coins   = [2]
    amount  = 3
    output  = -1

    solution = CoinChange(coins, amount)

    assert solution.solve() == output


    #Test 3
    coins   = [1]
    amount  = 0
    output  = 0

    solution = CoinChange(coins, amount)

    assert solution.solve() == output


    #Test 4
    coins   = [2,5,10,1]
    amount  = 27
    output  = 4

    solution = CoinChange(coins, amount)

    assert solution.solve() == output


    #Test 5
    coins   = [186,419,83,408]
    amount  = 6249
    output  = 20

    solution = CoinChange(coins, amount)

    assert solution.solve() == output