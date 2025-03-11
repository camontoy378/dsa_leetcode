import setup_paths

from lc_104_max_depth_bt import MaxDepthBinaryTree


def test_solve():

    #Test 1
    root    = [3]
    output  = 1

    my_search = MaxDepthBinaryTree(root)

    assert my_search.solve() == output

    #Test 2
    root    = [3,9,20,None,None,15,7]
    output  = 3

    my_search = MaxDepthBinaryTree(root)

    assert my_search.solve() == output

    #Test 3
    root    = [1,None,2]
    output  = 2

    my_search = MaxDepthBinaryTree(root)

    assert my_search.solve() == output
    