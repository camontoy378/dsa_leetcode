import setup_paths
from lc_463_island_perimeter import IslandPerimeter

def test_get_inital_valid_indexes():

    #Test 1
    input   = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    output  = 0,1

    row_length      = len(input)
    column_length   = len(input[0])

    solution = IslandPerimeter(input)

    assert solution.get_inital_valid_indexes(row_length, column_length) == output


def test_get_valid_neighbor():

    #Test 1
    input       = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    
    index_row       = 0
    index_column    = 1
    row_length      = len(input)
    column_length   = len(input[0])

    output          = [[1,1]]

    solution        = IslandPerimeter(input)

    assert solution.get_valid_neighbors(index_row, index_column, row_length, column_length) == output

    #Test 2
    index_row       = 2
    index_column    = 1

    output          = [[1,1],[3,1]]

    assert solution.get_valid_neighbors(index_row, index_column, row_length, column_length) == output

    #Test 3
    input           = [[1,0]]
    
    index_row       = 0
    index_column    = 0
    row_length      = len(input)
    column_length   = len(input[0])

    output          = []

    solution        = IslandPerimeter(input)

    assert solution.get_valid_neighbors(index_row, index_column, row_length, column_length) == output




def test_solve():

    #Test 1
    input   = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    output  = 16

    solution = IslandPerimeter(input)

    assert solution.solve() == output

    #Test 2
    
    input   = [[1]]
    output  = 4

    solution = IslandPerimeter(input)

    assert solution.solve() == output

    #Test 3
    input   = [[1,0]]
    output  = 4

    solution = IslandPerimeter(input)

    assert solution.solve() == output
    