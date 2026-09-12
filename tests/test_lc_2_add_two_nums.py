import setup_paths

from lc_2_add_two_nums import AddTwoNums

def test_solve():

    #Test 1
    l1      = [2,4,3]
    l2      = [5,6,4]
    output  = [7,0,8]

    solution = AddTwoNums(l1, l2)

    assert solution.solve().val == output[0]

    #Test 2
    l1      = [0]
    l2      = [0]
    output  = [0]

    solution = AddTwoNums(l1, l2)

    assert solution.solve().val == output[0]

    #Test 3
    l1      = [9,9,9,9,9,9,9]
    l2      = [9,9,9,9]
    output  = [8,9,9,9,0,0,0,1]

    solution = AddTwoNums(l1, l2)

    assert solution.solve().next.val == output[1]