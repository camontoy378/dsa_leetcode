class SumSubarrayMinimuns():

    def __init__(self, int_arr):
        self.int_arr    = int_arr

    def solve(self):

        sum : int = 0

        size_num_array = len(self.int_arr) 

        for i_index in range(size_num_array):
            sum         += self.int_arr[i_index]
            current_min =  self.int_arr[i_index]

            for j_index in range(i_index + 1, size_num_array):
                if  current_min > self.int_arr[j_index]:
                    current_min = self.int_arr[j_index]

                sum += current_min

        if sum > 10**9:
            result = int(sum / (10**9))
            return (sum % (10**9) - (7 * result))
        else:
            return sum
        