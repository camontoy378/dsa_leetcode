import setup_paths

from lc_206_reverse_ll import ReverseLinkedList_iter

def test_solve():

    #Test 1

    input   = [1,2,3,4,5]
    output  = [5,4,3,2,1]

    solution = ReverseLinkedList_iter(input)

    assert solution.solve() == output

    #Test 2

    input   = [1,2]
    output  = [2,1]

    solution = ReverseLinkedList_iter(input)

    assert solution.solve() == output

    #Test 3

    input   = []
    output  = []

    solution = ReverseLinkedList_iter(input)

    assert solution.solve() == output