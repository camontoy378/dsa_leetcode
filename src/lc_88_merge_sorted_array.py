class MergeSortedArray():

    def __init__(self, nums1, nums2, m, n):
        self.nums1     = nums1
        self.nums2     = nums2
        self.m              = m
        self.n              = n

    def merge_sorted_array(self):
        
        pt_arr_1    = self.m - 1
        pt_arr_2    = self.n - 1
        len_array_1 = self.m + self.n - 1

        if self.n == 0:
            return
        
        for index_end in range(len_array_1,-1,-1):
            
            if ( self.nums1[pt_arr_1] > self.nums2[pt_arr_2]  and  pt_arr_1 >= 0 )  or pt_arr_2 < 0:
                
                self.nums1[index_end] = self.nums1[pt_arr_1]
                
                pt_arr_1 -= 1

            else:
                self.nums1[index_end] = self.nums2[pt_arr_2]
                pt_arr_2 -= 1

        return

    def solve(self):

        self.merge_sorted_array()
        return self.nums1