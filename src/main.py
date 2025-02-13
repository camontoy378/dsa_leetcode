from lc_20_valid_parenthesis import ValidParenthesis
from lc_1652_defuse_bomb import DefuseBomb
from lc_3318_find_xsum_of_klong_subarrays import FindXsumKlongSubarray
from lc_21_merge_two_sorted_lists import Merge2SortedLists
from lc_643_max_avg_subarray import MaxAvgSubarray
from lc_35_search_insert_position import SearchInsertPosition

def main():

    input_list  = [10,5,7,7,3,2,10,3,6,9,1,6]
    k           = -4

    input_list  = [1,1,2,2,3,4,2,3]
    k           = 6
    x           = 2

    list1   = [1,2,4]
    list2   = [1,3,4]

    nums    = [4,2,1,3,3]
    k       = 2

    input_list  = [1,3,5,6]
    target_num  = 7

    #solution = ValidParenthesis(input)
    #solution = DefuseBomb(input_list, k)
    #solution = FindXsumKlongSubarray(input_list, k, x)
    #solution = Merge2SortedLists(list1, list2)
    #solution = MaxAvgSubarray(nums, k)
    solution = SearchInsertPosition(input_list, target_num)

    solution.solve()

if __name__ == "__main__":
    main()