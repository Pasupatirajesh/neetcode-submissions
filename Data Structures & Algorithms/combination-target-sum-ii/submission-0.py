class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(index, path_sum, path):
            if path_sum == target:
                res.append(path[:])
                return
            
            if path_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path_sum+candidates[i], path)
                path.pop()
        backtrack(0, 0, [])
        return res