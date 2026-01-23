class KthLargestElement():

    def __init__(self, nums, k):
        self.nums   = nums
        self.k      = k

    def heap_min_balance_tree_td(self, i, nums, k):
        
        left_child  = (2 * i) + 1
        right_child = (2 * i) + 2
        
        #No children
        if left_child >= k:
            return
        
        #No right child
        elif right_child >= k:
            if nums[left_child] < nums[i]:
                self.swap(left_child, i, nums)
                self.heap_min_balance_tree_td(left_child, nums, k)
        else:
            if nums[left_child] < nums[right_child]:
                if nums[left_child] < nums[i]:
                    self.swap(left_child, i, nums)
                    self.heap_min_balance_tree_td(left_child, nums, k)
            else:
                if nums[right_child] < nums[i]:
                    self.swap(right_child, i, nums)
                    self.heap_min_balance_tree_td(right_child, nums, k)

    def heap_min_delete(self, i, nums, k):
        
        #Pop and replace root node
        nums[0] = nums[i]

        #Balance tree top down.
        self.heap_min_balance_tree_td(0, nums, k)

    def heap_min_insert(self, i, nums):
        #Navigating tree via array
        #Current node = i
        #Left child   = 2 * i + 1
        #Right child   = 2 * i + 2
        #Parent       = (i - 1) / 2  ##Integer value 

        parent_index = int ((i - 1) / 2)

        #If parent doesn't exist: 
        if parent_index < 0:
            return
        
        if nums[i] < nums[parent_index]:
            self.swap(i, parent_index, nums)
            self.heap_min_insert(parent_index, nums)
    
    def swap(self, i, j, nums):
        temp       = nums[i]
        nums[i]    = nums[j]
        nums[j]    = temp
    

    def solve(self):

        k       = self.k
        nums    = self.nums

        for i in range(0,k):
            #Fix heap min tree
            self.heap_min_insert(i, nums)

        for i in range(k, len(nums)):
            
            #Compare num againts root number.
            if nums[0] < nums[i]:
                self.heap_min_delete(i, nums, k )

        return nums[0]