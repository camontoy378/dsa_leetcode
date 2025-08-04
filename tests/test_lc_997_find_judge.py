import setup_paths

from lc_997_find_judge import FindJudge

def test_solve():

    #Test 1
    n       = 2 
    trust   = [[1,2]]
    output  = 2

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    #Test 2
    n       = 3 
    trust   = [[1,3],[2,3]]
    output  = 3

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    #Test 3
    n       = 3 
    trust   = [[1,3],[2,3],[3,1]]
    output  = -1

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    #Test 4
    n       = 4 
    trust   = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    output  = 3

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    #Test 5
    n       = 3 
    trust   = [[1,2],[2,3]]
    output  = -1

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    #Test 6
    n       = 4 
    trust   = [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]
    output  = 3

    solution = FindJudge(n, trust)

    assert solution.solve() == output

    
