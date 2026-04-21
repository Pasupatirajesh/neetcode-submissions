class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        # subset = []
        result = []
        
        def backtrack(st, subset):
             
            result.append(subset.copy())
            
            for i in range(st, n):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()                    
        
        backtrack(0, [])
        return result



        