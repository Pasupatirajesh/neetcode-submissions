class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        num_sum = 0
        for i in range(len(nums)):
            if num_sum < 0:
                num_sum = max(num_sum, 0)
            num_sum+=nums[i]
            res = max(res, num_sum)
        return res 
