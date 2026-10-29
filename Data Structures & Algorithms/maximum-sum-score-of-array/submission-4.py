class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        
        total = sum(nums)
        ans = total
        prefix_before_i = suffix_from_i = 0
        for i in range(len(nums)):
            
            suffix_from_i = total - (prefix_before_i)
            
            prefix_through_i = prefix_before_i + nums[i]

            ans = max(ans, max(suffix_from_i, prefix_through_i))
            prefix_before_i += nums[i]
        return ans 
            
