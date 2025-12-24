class NextGreaterElement1():

    def __init__(self, nums1:list, nums2:list):
        self.nums1  = nums1
        self.nums2  = nums2

    def solve(self):

        #Initialize
        nums1_len = len(self.nums1)
        nums2_len = len(self.nums2)
        output2_dict = {}
        output1_list = [-1] * nums1_len
        stack = []

        for i in range(nums2_len):
            
            while stack and (self.nums2[i] > self.nums2[stack[-1]]):
                print(f"current_num = {self.nums2[i]}")
                output2_dict[self.nums2[stack[-1]]] = self.nums2[i]
                stack.pop()

            stack.append(i)
        print(output2_dict)
        for i in range(nums1_len):
            if self.nums1[i] in output2_dict:
                output1_list[i] = output2_dict[self.nums1[i]]

        return output1_list