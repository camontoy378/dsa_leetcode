
class KthMissingPositiveNumber():

    def __init__(self, nums_list, k):
        self.nums_list  = nums_list
        self.k          = k

    def solve(self):

        arr = self.nums_list
        k   = self.k

        max_array_size = 1000


        missing = []

        for i in range(1, 2 * max_array_size + 1):
            if i not in arr:
                missing.append(i)
                if len(missing) == k:
                    return missing[-1]

        return None