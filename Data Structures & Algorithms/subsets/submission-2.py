class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        # subset = []
        result = []
        
        def backtrack(i, subset):
            if i == n:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()                    
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return result



        