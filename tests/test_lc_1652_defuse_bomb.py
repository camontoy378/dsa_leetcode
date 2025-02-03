import setup_paths

from lc_1652_defuse_bomb import DefuseBomb

def test_solve():
    
    #Test 1
    input_list  = [5,7,1,4]
    k           = 3
    output      = [12,10,16,13]

    my_defuse = DefuseBomb(input_list, k)

    assert my_defuse.solve() == output

    #Test 2
    input_list  = [1,2,3,4]
    k           = 0
    output      = [0,0,0,0]

    my_defuse.input_list    = input_list
    my_defuse.k             = k

    assert my_defuse.solve() == output

    #Test 3
    input_list  = [2,4,9,3]
    k           = -2
    output      = [12,5,6,13]

    my_defuse.input_list    = input_list
    my_defuse.k             = k

    assert my_defuse.solve() == output

    #Test 4
    input_list  = [5,2,2,3,1]
    k           = 3
    output      = [7,6,9,8,9]

    my_defuse.input_list    = input_list
    my_defuse.k             = k

    assert my_defuse.solve() == output

    #Test 5
    input_list  = [10,5,7,7,3,2,10,3,6,9,1,6] ##12
    k           = -4
    output      = [22,26,22,28,29,22,19,22,18,21,28,19]

    my_defuse.input_list    = input_list
    my_defuse.k             = k

    assert my_defuse.solve() == output




    