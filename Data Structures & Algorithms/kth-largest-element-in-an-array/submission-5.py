import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select similar to quick sort 
        #avergae O(n) and worst case O(n**2)
        k = len(nums) -k 
        l , r = 0, len(nums) -1
        while l < r:
            p_ = random.randint(l, r)
            p = self.quickselect(nums,l,r, p_)
            if p < k:
                l = p + 1
            elif p > k:
                r = p-1
            else:
                break
        return nums[k]
       

    def quickselect(self,nums,l,r, p_):
        pivot= nums[p_]
        nums[p_], nums[r] = nums[r], nums[p_]
        p = l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p+=1
        nums[p], nums[r] = nums[r], nums[p]
        return p
        
    

        
    

        

        