import setup_paths

from lc_253_meeting_rooms_2 import MeetingRoomsTwo

def test_solve():

    #Test 1
    intervals   = [[0,30],[5,10],[15,20]]
    output      = 2

    solution = MeetingRoomsTwo(intervals)

    assert solution.solve() == output

    #Test 2
    intervals   = [[7,10],[2,4]]
    output      = 1

    solution = MeetingRoomsTwo(intervals)

    assert solution.solve() == output