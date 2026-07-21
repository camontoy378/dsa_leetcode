import setup_paths

from lc_228_summary_ranges import SummaryRanges

def test_solve():

    #Test 1
    nums    = [0,1,2,4,5,7]
    output  = ["0->2","4->5","7"]

    solution = SummaryRanges(nums)

    assert solution.solve() == output


    #Test 1
    nums    = [0,2,3,4,6,8,9]
    output  = ["0","2->4","6","8->9"]

    solution = SummaryRanges(nums)

    assert solution.solve() == output