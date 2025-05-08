import setup_paths

from lc_733_flood_fill import FloodFill

def test_solve():

    #Test 1
    image   = [[1,1,1],[1,1,0],[1,0,1]]
    sr      = 1
    sc      = 1
    color   = 2

    output  = [[2,2,2],[2,2,0],[2,0,1]]

    solution = FloodFill(image, sr, sc, color)

    assert solution.solve() == output

    #Test 2
    image   = [[0,0,0],[0,0,0]]
    sr      = 0
    sc      = 0
    color   = 0

    output  = [[0,0,0],[0,0,0]]

    solution = FloodFill(image, sr, sc, color)

    assert solution.solve() == output