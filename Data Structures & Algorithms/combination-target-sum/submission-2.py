class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res =[]

        def backtrack(index, path_sum, path):
            if path_sum == target:
                res.append(path.copy())
                return
            if path_sum > target:
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, path_sum+nums[i], path)
                path.pop()
            
        backtrack(0, 0, [])
        return res
            


