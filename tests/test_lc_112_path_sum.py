import setup_paths

from lc_112_path_sum import PathSum
from make_tree import MakeTree

def test_solve():

    #Test 1
    root        = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum   = 22
    
    solution = PathSum(root, targetSum)

    assert solution.solve() == True

    #Test 2
    root            = [1,2,3]
    expected_value  = 5

    solution = PathSum(root, targetSum)

    assert solution.solve() == False

    #Test 3
    root            = []
    expected_value  = 0

    solution = PathSum(root, targetSum)

    assert solution.solve() == False


def test_tree_trasverse():

    #Test 1
    input           = [1,2,3]
    expected_value  = 3

    i       = 0
    n       = len(input)
    sum     = 0


    solution = PathSum(input, expected_value)

    mytree = MakeTree(input)

    root = mytree.insert_level_order(i, n)

    assert solution.tree_trasverse(root, expected_value, sum, False) == True

    #Test 2
    expected_value = 5

    assert solution.tree_trasverse(root, expected_value, sum, False) == False

    #Test 3
    input           = [1,None,3]
    expected_value  = 4

    i       = 0
    n       = len(input)
    sum     = 0


    solution = PathSum(input, expected_value)

    mytree = MakeTree(input)

    root = mytree.insert_level_order(i, n)

    assert solution.tree_trasverse(root, expected_value, sum, False) == True