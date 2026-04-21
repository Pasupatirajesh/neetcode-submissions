class Solution:
    def rob(self, nums: List[int]) -> int:
        first = nums[:-1]
        sec = nums[1:]
        if len(nums) == 1:
            return nums[0]
        def rob_lin(houses):
            dp = [-1] * (len(houses) + 1)

            def memo(i):
                if i >= len(houses):
                    return 0
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(houses[i] + memo(i+2) , memo(i+1))
                return dp[i]
            return memo(0)
        return max(rob_lin(first), rob_lin(sec))