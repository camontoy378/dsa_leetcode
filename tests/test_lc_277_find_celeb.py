import setup_paths

from lc_277_find_celeb import FindCeleb

def test_knows():

    #Test 1

    graph   = [[1,1,0],[0,1,0],[1,1,1]]
    a       = 0
    b       = 1
    output  = True

    solution = FindCeleb(graph)

    assert  solution.knows(a, b) == output

    #Test 2
    a       = 1
    b       = 2
    output  = False

    assert  solution.knows(a, b) == output

def test_solve():

    #Test 1

    graph   = [[1,1,0],[0,1,0],[1,1,1]]
    output  = 1

    solution = FindCeleb(graph)

    assert solution.solve() == output


    #Test 2

    graph   = [[1,0,1],[1,1,0],[0,1,1]]
    output  = -1

    solution = FindCeleb(graph)

    assert solution.solve() == output

    #Test 3

    graph   = [[1,0],[0,1]]
    output  = -1

    solution = FindCeleb(graph)

    assert solution.solve() == output

    #Test 4

    graph   = [[1,0],[1,1]]
    output  = 0

    solution = FindCeleb(graph)

    assert solution.solve() == output