import setup_paths

from lc_19_remove_nth_node import RemoveNthNodeFromEnd, LinkedList

def test_solve():

    #Test 1
    head    = [1,2,3,4,5]
    n       = 2
    output  = [1,2,3,5]

    my_ll_2 = LinkedList()
    my_ll_2.create_ll(head)
    my_ll_2.print_ll()

    solution = RemoveNthNodeFromEnd(my_ll_2.head, n)
    solution.solve()

    assert solution.output() == output

    #Test 2
    head    = [1]
    n       = 1
    output  = []

    my_ll_2 = LinkedList()
    my_ll_2.create_ll(head)
    my_ll_2.print_ll()
    
    solution = RemoveNthNodeFromEnd(my_ll_2.head, n)
    solution.solve()

    assert solution.output() == output

    #Test 3
    head    = [1,2]
    n       = 1
    output  = [1]

    my_ll_2 = LinkedList()
    my_ll_2.create_ll(head)
    my_ll_2.print_ll()

    solution = RemoveNthNodeFromEnd(my_ll_2.head, n)
    solution.solve()

    assert solution.output() == output