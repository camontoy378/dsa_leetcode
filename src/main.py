from lc_20_valid_parenthesis import ValidParenthesis
from lc_1652_defuse_bomb import DefuseBomb
from lc_3318_find_xsum_of_klong_subarrays import FindXsumKlongSubarray
from lc_21_merge_two_sorted_lists import Merge2SortedLists
from lc_643_max_avg_subarray import MaxAvgSubarray
from lc_35_search_insert_position import SearchInsertPosition

from lc_100_same_tree import SameTree
from lc_100_same_tree import TreeNode

from lc_112_path_sum import PathSum

from make_tree import *

def main():

    input   = [1,2,3]
    i       = 0
    n       = len(input)
    expected_value = 3
    sum     = 0

    solution = PathSum(input)
    mytree = MakeTree(input)

    root = mytree.insert_level_order(i, n)

    output = solution.tree_trasverse(root, expected_value, sum, False)
    print(f"output = {output}")

    #solution.solve()

if __name__ == "__main__":
    main()