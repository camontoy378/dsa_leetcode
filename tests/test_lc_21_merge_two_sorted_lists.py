import setup_paths

from lc_21_merge_two_sorted_lists import Merge2SortedLists

def test_solve():

    #Test 1
    list1   = [1,2,4]
    list2   = [1,3,4]
    
    output  = [1,1,2,3,4,4]

    solution = Merge2SortedLists(list1, list2)
    
    assert solution.solve() == output

    #Test 2
    solution.list1 = []
    solution.list2 = []

    output = []

    assert solution.solve() == output

    #Test 3
    solution.list1 = []
    solution.list2 = [0]

    output = [0]

    assert solution.solve() == output
