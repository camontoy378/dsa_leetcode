import setup_paths

from lc_543_diameter_binary_tree import DiameterBinaryTree

def test_solve():

    #Test 1
    input   = [1,2,3,4,5]
    output  = 3

    solution = DiameterBinaryTree(input)
    
    assert solution.solve() == output


    #Test 2
    input   = [1,2]
    output  = 1

    solution = DiameterBinaryTree(input)
    
    assert solution.solve() == output

    #Test 3
    input   = [4,2,None,3,1,None,None,None,None,5,None]
    output  = 3

    solution = DiameterBinaryTree(input)
    
    assert solution.solve() == output


    #Test 4

    input   = [4,2,None,1,3]
    output  = 2

    solution = DiameterBinaryTree(input)
    
    assert solution.solve() == output

    #Test 5

    input   = [1,None,3]
    output  = 1

    solution = DiameterBinaryTree(input)
    
    assert solution.solve() == output
