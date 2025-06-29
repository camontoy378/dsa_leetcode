import setup_paths
from lc_1086_high_five import HighFive


def test_solve():

    #Test 1
    input   = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    output  = [[1,87],[2,88]]

    solution = HighFive(input)

    assert solution.solve() == output


    #Test 2
    input   = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    output  = [[1,100],[7,100]]

    solution = HighFive(input)

    assert solution.solve() == output

    #Test 3
    input   = [[1,84],[1,72],[1,47],[1,43],[1,78], [2,79],[2,4] ,[2,23],[2,88],[2,79], [3,75],[3,80],[3,38],[3,73],[3,4]]
    
    output  = [[1,64],[2,54],[3,54]]

    solution = HighFive(input)

    assert solution.solve() == output
