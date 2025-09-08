import setup_paths

from lc_1762_ocean_view import OceanView

def test_solve():

    #Test 1
    heights = [4,2,3,1]
    output  = [0,2,3]

    solution = OceanView(heights)

    assert solution.solve() == output

    #Test 2
    heights = [4,3,2,1]
    output  = [0,1,2,3]

    solution = OceanView(heights)

    assert solution.solve() == output

    #Test 3
    heights = [1,3,2,4]
    output  = [3]

    solution = OceanView(heights)

    assert solution.solve() == output