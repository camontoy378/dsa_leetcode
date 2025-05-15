import setup_paths
from lc_101_symmetric_tree import SymmetricTree

def test_solve_array():

    #Test 1
    input       = [1,2,2,3,4,4,3]
    output      = True

    solution = SymmetricTree(input)

    assert solution.solve_array() == output


    #Test 2
    input       = [1,2,2,None,3,None,3]
    output      = False

    solution = SymmetricTree(input)

    assert solution.solve_array() == output


def test_solve_tree():

    #Test 1
    input       = [1,2,2,3,4,4,3]
    output      = True

    solution = SymmetricTree(input)

    assert solution.solve_tree() == output

    #Test 2
    input       = [1,2,2,None,3,None,3]
    output      = False

    solution = SymmetricTree(input)

    assert solution.solve_tree() == output 
