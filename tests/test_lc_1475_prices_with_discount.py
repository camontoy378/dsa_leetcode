import setup_paths

from lc_1475_prices_with_discount import PricesWithDiscount

def test_solve():

    #Test 1
    prices  = [8,4,6,2,3]
    output  = [4,2,4,2,3]
    
    solution = PricesWithDiscount(prices)

    assert solution.solve() == output

    #Test 2
    prices  = [1,2,3,4,5]
    output  = [1,2,3,4,5]
    
    solution = PricesWithDiscount(prices)

    assert solution.solve() == output

    #Test 3
    prices  = [10,1,1,6]
    output  = [9,0,1,6]
    
    solution = PricesWithDiscount(prices)

    assert solution.solve() == output

    #Test 4
    prices  = [4,7,1,9,4,8,8,9,4]
    output  = [3,6,1,5,0,0,4,5,4]
    
    solution = PricesWithDiscount(prices)

    assert solution.solve() == output