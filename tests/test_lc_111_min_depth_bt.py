import setup_paths

from lc_111_min_depth_bt import MinDepthBT
from lc_111_min_depth_bt import TreeNode

def test_get_adj_dict():

    #Test 1
    input   = [3,9,20,None,None,15,7]
    output  = 2

    adj_dict = {}

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    solution = MinDepthBT(root)

    solution.get_adj_dict(adj_dict, root)

    assert adj_dict[3]  == [9,20]
    assert adj_dict[20] == [15,7]
    assert adj_dict[15] == []

    #Test 2
    input   = [2,None,3,None,4,None,5,None,6]
    output  = 5

    adj_dict = {}

    root = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)  ) )) )

    solution = MinDepthBT(root)

    solution.get_adj_dict(adj_dict, root)

    assert adj_dict[2] == [3]
    assert adj_dict[5] == [6]
    assert adj_dict[6] == []

def test_solve_bfs():

    #Test 1
    input   = [3,9,20,None,None,15,7]
    output  = 2

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    solution = MinDepthBT(root)

    assert solution.solve_bfs() == output

    #Test 2
    input   = [2,None,3,None,4,None,5,None,6]
    output  = 5

    adj_dict = {}

    root = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)  ) )) )

    solution = MinDepthBT(root)

    assert solution.solve_bfs() == output



def test_solve_dfs():

    #Test 1
    input   = [3,9,20,None,None,15,7]
    output  = 2

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    solution = MinDepthBT(root)

    assert solution.solve_dfs() == output