class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = i
        gp = 0
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] == nums[j]:
                    gp+=1
        return gp 