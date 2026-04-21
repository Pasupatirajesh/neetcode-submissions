class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            l = i+1 
            r = len(nums)-1
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            while l< r:
                
                summ = nums[l] + a + nums[r]
                if summ < 0:
                    l+=1
                elif summ > 0:
                    r-=1
                else:
                    res.append([nums[l], a, nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res 
                

                

        