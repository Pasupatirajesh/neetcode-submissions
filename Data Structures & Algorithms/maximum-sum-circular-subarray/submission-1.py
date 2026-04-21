class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_kadane, min_kadane = nums[0], nums[0]
        cur_max, cur_min = 0, 0

        for i in range(len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_kadane = max(max_kadane, cur_max)
            
            cur_min = min(nums[i], cur_min + nums[i])
            min_kadane = min(min_kadane, cur_min)


        total_sum = sum(nums)

        if max_kadane < 0:
            return max_kadane

        return max(max_kadane, total_sum-min_kadane)            