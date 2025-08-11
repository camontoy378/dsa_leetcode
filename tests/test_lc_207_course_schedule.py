import setup_paths

from lc_207_course_schedule import CourseSchedule

def test_build_adjacency_graph():

    #Test 1
    numCourses      = 2 
    prerequisites   = [[1,0], [2,0], [2,1]]
    output          = {0:[1,2], 1:[2], 2:[]}

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.build_adjacency_graph() == output

    #Test 1
    numCourses      = 2 
    prerequisites   = [[5,5]]
    output          = {5:[5], 5:[5]}

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.build_adjacency_graph() == output

def test_solve():

    #Test 1
    numCourses      = 2 
    prerequisites   = [[1,0]]
    output          = True

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 2
    numCourses      = 2 
    prerequisites   = [[1,0],[0,1]]
    output          = False

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 3
    numCourses      = 5 
    prerequisites   = [[1,4],[2,4],[3,1],[3,2]]
    output          = True

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 4
    numCourses      = 1 
    prerequisites   = []
    output          = True

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 5
    numCourses      = 20
    prerequisites   = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    output          = False

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output
        
    #Test 6
    numCourses      = 2
    prerequisites   = [[5,5]]
    output          = False

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 7
    numCourses      = 3 
    prerequisites   = [[0,2],[1,2],[2,0]]
    output          = False

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output

    #Test 8
    numCourses      = 3 
    prerequisites   = [[1,0],[2,0],[0,2]]
    output          = False

    solution = CourseSchedule(numCourses, prerequisites)

    assert solution.solve() == output
    