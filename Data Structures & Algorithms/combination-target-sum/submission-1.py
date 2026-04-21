class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return 
            # include val at nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            # exclude val at nums[i]
            dfs(i+1, curr, total)
        dfs(0, curr, 0)
        return res
        