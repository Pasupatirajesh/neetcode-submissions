class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            left = arr[L:M]
            right = arr[M:R]
            j = 0
            k = 0
            i = L
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k < len(right):
                arr[i] = right[k]
                k+=1
                i+=1

        def mergesort(arr, L, R):
            if L >= R-1:
                return 
            M = (L+R) //2
            mergesort(arr, L, M)
            mergesort(arr, M, R)
            merge(arr, L, M, R)
        
        mergesort(nums, 0, len(nums))
        return nums
