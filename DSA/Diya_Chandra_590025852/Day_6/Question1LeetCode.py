class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            rob_prev = 0     
            rob_before = 0    

            for money in houses:
                current = max(rob_prev, rob_before + money)

                rob_before = rob_prev
                rob_prev = current

            return rob_prev

        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:])   
        )
        