import heapq

class MeetingRoomsTwo():

    def __init__(self, int_array):
        self.int_array = int_array

    def solve(self):

        num_rooms_needed = 0
        end_times_arr = []

        #Sort input based on start times
        heapq.heapify(self.int_array)

        #Solve num meeting rooms based on sorted end times.
        while len(self.int_array) > 0:
            time_slot = heapq.heappop(self.int_array)

            if len(end_times_arr) == 0:
                num_rooms_needed += 1
                heapq.heappush(end_times_arr,time_slot[1])
            elif time_slot[0] < end_times_arr[0]:
                num_rooms_needed += 1
                heapq.heappush(end_times_arr,time_slot[1])
            else:
                #A room is available
                heapq.heappop(end_times_arr)
                heapq.heappush(end_times_arr, time_slot[1])
            
        return num_rooms_needed
