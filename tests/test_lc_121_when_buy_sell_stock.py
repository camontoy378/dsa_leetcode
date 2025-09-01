import setup_paths

from lc_121_when_buy_sell_stock import WhenBuySellStock

def test_solve():

    #Test 1
    prices = [7,1,5,3,6,4]
    output = 5

    solution = WhenBuySellStock(prices)

    assert solution.solve() ==  output

    #Test 2
    prices = [7,6,4,3,1]
    output = 0

    solution = WhenBuySellStock(prices)

    assert solution.solve() == output