class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums) + 1)
        n =len(nums)
        def memoization(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(memoization(i+1), nums[i] + memoization(i+2))
            return cache[i]
        return memoization(0) 
            