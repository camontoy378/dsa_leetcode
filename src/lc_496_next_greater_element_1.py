class NextGreaterElement1():

    def __init__(self, nums1:list, nums2:list):
        self.nums1  = nums1
        self.nums2  = nums2

    def solve(self):

        #Initialize
        nums1_len = len(self.nums1)
        nums2_len = len(self.nums2)
        map_num_to_next_greater_num = {}
        output1_list = [-1] * nums1_len

        #Stack contains indexes of nums2
        stack = []

        for i in range(nums2_len):

            current_num_from_nums2 = self.nums2[i]
            if stack:
                num_top_stack = self.nums2[stack[-1]]
            
            while stack and (current_num_from_nums2 > num_top_stack):
                map_num_to_next_greater_num[num_top_stack] = current_num_from_nums2
                stack.pop()

            stack.append(i)

        for i in range(nums1_len):
            if self.nums1[i] in map_num_to_next_greater_num:
                output1_list[i] = map_num_to_next_greater_num[self.nums1[i]]

        return output1_list