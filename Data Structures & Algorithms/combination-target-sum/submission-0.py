class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, temp = [], []
        self.recur(nums, target, 0, ans, temp)
        return ans 
    
    def recur(self, nums, target, index, ans, temp):
        if target == 0:
            ans.append(temp[:])
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            temp.append(nums[i])
            self.recur(nums, target-nums[i], i, ans, temp)
            temp.pop()
    
        