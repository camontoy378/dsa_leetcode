import setup_paths
from lc_1971_find_path_in_graph import FindPathInGraph


def test_create_adj_dict():

    #Test 1
    num_nodes   = 3
    edges       = [[0,1],[1,2],[0,2]]
    source      = 0
    destination = 2

    output      = {0:[1,2], 1:[0,2], 2:[1,0]}

    solution = FindPathInGraph(num_nodes, edges, source, destination)

    assert solution.create_adj_dict(solution.edges) == output

def test_solve():

    #Test 1
    num_nodes   = 3
    edges       = [[0,1],[1,2],[0,2]]
    source      = 0
    destination = 2

    solution = FindPathInGraph(num_nodes, edges, source, destination)
    
    assert solution.solve() == True

    #Test 2
    num_nodes   = 6
    edges       = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source      = 0
    destination = 5

    solution = FindPathInGraph(num_nodes, edges, source, destination)
    
    assert solution.solve() == False