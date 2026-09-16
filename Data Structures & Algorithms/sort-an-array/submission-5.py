import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # L, R = 0, len(nums)-1
        def partition(nums, L, R):
            r = random.randint(L, R)
            nums[r], nums[R] = nums[R], nums[r]
            pivot = nums[R]
            i = L
            
            for j in range(L, R):
                if nums[j] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i+=1
            nums[i], nums[R] = nums[R], nums[i]
            return i 
        
        def quicksort(nums, L, R):
            if L >= R:
                return 
            p = partition(nums, L, R)
            quicksort(nums, L, p-1)
            quicksort(nums, p+1, R)
        quicksort(nums, 0, len(nums)-1)
        return nums
