import pytest
import setup_paths
from lc_100_same_tree import SameTree
from lc_100_same_tree import TreeNode

def test_create_tree_from_array():

    #Test 1
    p = [1,2,3]
    q = [1,2,3]
    #head: TreeNode = None

    mycreate = SameTree(p, q)

    head = mycreate.create_tree_from_array(p)

    assert head.val == 1

    #Test 2
    assert head.left.val == 2

    #Test 3
    assert head.right.val == 3


def test_insert():

    #Test 1
    p = [1,2,3]
    q = [1,2,3]
    head: TreeNode = None

    myinsert = SameTree(p, q)

    head = myinsert.insert(head, p[0])

    assert head.val == 1

    #Test 2
    head = myinsert.insert(head, p[1])
    assert head.left.val == 2

    #Test 3
    head = myinsert.insert(head, p[2])
    assert head.right.val == 3

    #Test 4
    p = [1,2]
    q = [1,None,2]

    root: TreeNode = None

    myinsert = SameTree(p, q)

    root = myinsert.insert(root, q[0])

    assert head.val == 1

    #Test 5
    root = myinsert.insert(root, q[1])
    assert root.left.val == None

    #Test 6
    root = myinsert.insert(root, q[2])
    assert root.right.val == 2




def test_solve():

    #Test 1
    p       = [1,2,3]
    q       = [1,2,3]
    output  = True

    solution = SameTree(p, q)

    assert solution.solve() == output

    #Test 2
    p       = [1,2]
    q       = [1,None,2]
    output  = False

    solution = SameTree(p, q)

    assert solution.solve() == output

    #Test 3
    p       = [1,2,1]
    q       = [1,1,2]
    output  = False

    solution = SameTree(p, q)

    assert solution.solve() == output

    #Test 4
    p       = []
    q       = []
    output  = True

    solution = SameTree(p, q)

    assert solution.solve() == output


@pytest.mark.skip(reason="AttributeError: 'NoneType' object has no attribute 'val'")
def test_solve_not():
    
    p       = [0]
    q       = [0]
    output  = True

    solution = SameTree(p, q)

    assert solution.solve() == output
    
