class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_kadane, min_kadane = nums[0], nums[0]
        cur_max, cur_min = 0, 0

        total_sum = sum(nums)

        for i in range(len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            max_kadane = max(max_kadane, cur_max)
            cur_min = min(cur_min + nums[i] , nums[i])
            min_kadane = min(min_kadane, cur_min)
        
        if  max_kadane < 0:
            return max_kadane
        return max(max_kadane, (total_sum - min_kadane))
    
