class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select similar to quick sort 
        #avergae O(n) and worst case O(n**2)
        self.nums = nums
        self.k = len(nums)-k
        return self.quickselect(0, len(nums)-1)

    def quickselect(self,l,r):
        pivot, p = self.nums[r], l
        for i in range(l, r):
            if self.nums[i] <= pivot:
                self.nums[p], self.nums[i] = self.nums[i], self.nums[p]
                p+=1
        self.nums[p], self.nums[r] = self.nums[r], self.nums[p]
        if p > self.k:
            return self.quickselect(l, p -1)
        elif p <self.k:
            return self.quickselect(p+1, r)
        else:
            return self.nums[p]
    

        
    

        

        