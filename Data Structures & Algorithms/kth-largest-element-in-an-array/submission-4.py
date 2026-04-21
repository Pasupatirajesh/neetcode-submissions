class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select similar to quick sort 
        #avergae O(n) and worst case O(n**2)
        k = len(nums) -k 
        l , r = 0, len(nums) -1
        while l < r:
            p = self.quickselect(nums,l,r)
            if p < k:
                l = p + 1
            elif p > k:
                r = p-1
            else:
                break
        return nums[k]
       

    def quickselect(self,nums,l,r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p+=1
        nums[p], nums[r] = nums[r], nums[p]
        return p
        
    

        
    

        

        