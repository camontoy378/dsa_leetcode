import setup_paths

from lc_102_bt_level_order import BTLevelOrder

def test_solve():

    #Test 1
    root    = [3,9,20, None, None,15,7]
    output  = [[3],[9,20],[15,7]]

    solution = BTLevelOrder(root, "bfs")

    assert solution.solve() == output

    #Test 2
    root    = [1]
    output  = [[1]]

    solution = BTLevelOrder(root, "bfs")

    assert solution.solve() == output

    #Test 3
    root    = []
    output  = []

    solution = BTLevelOrder(root, "bfs")

    assert solution.solve() == output