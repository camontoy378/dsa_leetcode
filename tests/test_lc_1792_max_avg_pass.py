import setup_paths

from lc_1792_max_avg_pass import MaxAvgPass

def test_solve():

    #Test 1

    classes         = [[1,2],[3,5],[2,2]]
    extraStudents   = 2
    output          = 0.78333

    solution = MaxAvgPass(classes, extraStudents)

    assert solution.solve() == output

    #Test 2

    classes         = [[2,4],[3,9],[4,5],[2,10]]
    extraStudents   = 4
    output          = 0.53485

    solution = MaxAvgPass(classes, extraStudents)

    assert solution.solve() == output