import setup_paths

from lc_49_group_anagrams import GroupAnagrams

def test_solve():

    #Test 1

    strs    = ["eat","tea","tan","ate","nat","bat"]
    output  = [["eat","tea","ate"],["tan", "nat"],["bat"]]

    solution = GroupAnagrams(strs)

    
    assert solution.solve() == output

    #Test 2

    strs    = ["ac","d"]
    output  = [["ac"],["d"]]

    solution = GroupAnagrams(strs)

    
    assert solution.solve() == output