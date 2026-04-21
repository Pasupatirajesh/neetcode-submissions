class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums.sort()

        dp = [-1] * (len(nums))

        def memo(i):
            if i >= len(nums):
                return 0
                
            if dp[i] != -1:
                return dp[i]
            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + memo(j))
            dp[i] = res
            return res 
        n = len(nums)
        return max(memo(i) for i in range(n))