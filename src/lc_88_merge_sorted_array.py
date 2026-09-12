class MergeSortedArray():

    def __init__(self, nums1, nums2, m, n):
        self.nums1     = nums1
        self.nums2     = nums2
        self.m              = m
        self.n              = n

    def merge_sorted_array(self):
        
        nums1     = self.nums1
        nums2     = self.nums2
        m         = self.m
        n         = self.n
        
        pt_arr_1    = m - 1
        pt_arr_2    = n - 1
        pt_arr_3    = len(nums1) - 1

        if n == 0:
            return
        
        while (pt_arr_1 >= 0) and (pt_arr_2 >= 0):

            if nums1[pt_arr_1] > nums2[pt_arr_2]:
                nums1[pt_arr_3] = nums1[pt_arr_1]
                pt_arr_1 -= 1
                
            else:
                nums1[pt_arr_3] = nums2[pt_arr_2]
                pt_arr_2 -= 1
                
            pt_arr_3 -= 1

        while (pt_arr_1 >= 0):

            nums1[pt_arr_3] = nums1[pt_arr_1]
            pt_arr_1 -= 1   
            pt_arr_3 -= 1

        while (pt_arr_2 >= 0):
            nums1[pt_arr_3] = nums2[pt_arr_2]
            pt_arr_2 -= 1   
            pt_arr_3 -= 1
                
        return

    def solve(self):

        self.merge_sorted_array()
        return self.nums1