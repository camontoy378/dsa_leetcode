import setup_paths

from lc_56_merge_intervals import MergeIntervals

def test_merge():

    #Test 1

    input_1 = [[1,2]]
    input_2 = [[3,4]]
    output  = [[1,2], [3,4]]

    solution = MergeIntervals(input_1)

    assert solution.merge_arrays(input_1, input_2) == output


    #Test 2

    input_1 = [[1,3]]
    input_2 = [[2,6]]
    output  = [[1,6]]

    solution = MergeIntervals(input_1)

    assert solution.merge_arrays(input_1, input_2) == output

def test_solve():

    #Test 1
    input   = [[1,3],[2,6],[8,10],[15,18]]
    output  = [[1,6],[8,10],[15,18]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 2
    input   = [[1,4],[4,5]]
    output  = [[1,5]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 3
    input   = [[4,7],[1,4]]
    output  = [[1,7]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 4
    input   = [[1,4],[1,4]]
    output  = [[1,4]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 5
    input   = [[1,4],[0,0]]
    output  = [[0,0],[1,4]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 6
    input   = [[1,4],[0,2],[3,5]]
    output  = [[0,5]]

    solution = MergeIntervals(input)

    assert solution.solve() == output

    #Test 7
    input   = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    output  = [[1,3],[4,7]]

    solution = MergeIntervals(input)

    assert solution.solve() == output