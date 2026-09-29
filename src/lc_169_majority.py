class Solution:
    def majorityElement(self, nums) -> int:

        test = len(nums) * 0.5

        nums.sort()

        print(nums)

        cur_num = nums[0]
        freq = 1

        for num in nums[1:]:
            if freq > test:
                return cur_num
            elif cur_num != num:
                cur_num = num
                freq = 1
            else:
                freq += 1

        return cur_num