import setup_paths

from make_tree import *

def test_make_tree():

    #Test 1
    input   = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    i       = 0
    n       = len(input)

    solution = MakeTree(input)

    root = solution.insert_level_order(i, n)
    solution.print_in_order(root)

    assert root.val == 1

    #Test 2
    p = [1,2,3]
    i       = 0
    n       = len(p)

    solution.array = p

    root = solution.insert_level_order(i, n)
    solution.print_in_order(root)

    assert root.left.data == 2

    #Test 3
    assert root.right.data == 3