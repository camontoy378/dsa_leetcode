import pytest
import setup_paths
from lc_100_same_tree import SameTree

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

    #Test 5
    p       = [0]
    q       = [0]
    output  = True

    solution = SameTree(p, q)

    assert solution.solve() == output
   