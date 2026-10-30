class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = total
        prefix = 0
        for i in range(len(nums)):
            suffix = total - prefix
            prefix_through_i = prefix + nums[i]
            ans = max(ans, suffix, prefix_through_i)
            prefix += nums[i]
        return ans 
