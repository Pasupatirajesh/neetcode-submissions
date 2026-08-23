class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] % 2 == 0 and nums[j] % 2 != 0:
                pass
            elif nums[i] % 2 != 0 and nums[j] % 2 == 0:
                pass
            else:
                return False
            i+=1
            j+=1
        return True