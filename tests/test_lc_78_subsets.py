import setup_paths

from lc_78_subsets import Subsets

def test_solve():

    #Test 1
    nums    = [1,2,3]
    output  = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    #nums    = [1]
    #output  = [[],[1]]

    solution = Subsets(nums)

    assert solution.solve() == output


    #Test 2
    nums    = [0]
    output  = [[],[0]]

    solution = Subsets(nums)

    assert solution.solve() == output