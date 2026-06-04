import setup_paths

from lc_122_when_buy_sell_stock_2 import WhenBuySellStockTwo

def test_solve():

    #Test 1
    prices  = [7,1,5,3,6,4]
    output  = 7

    solution = WhenBuySellStockTwo(prices)

    assert solution.solve() == output

    #Test 2
    prices  = [1,2,3,4,5]
    output  = 4

    solution = WhenBuySellStockTwo(prices)

    assert solution.solve() == output

    #Test 3
    prices  = [7,6,4,3,1]
    output  = 0

    solution = WhenBuySellStockTwo(prices)

    assert solution.solve() == output