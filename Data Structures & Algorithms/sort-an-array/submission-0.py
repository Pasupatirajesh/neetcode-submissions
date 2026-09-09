class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            left, right = arr[L:M], arr[M:R]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i]= left[j]
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
    
        def mergesort(arr, l, r):
            if l>= r-1:
                return
            m = (l+r) // 2
            mergesort(arr,l, m)
            mergesort(arr, m, r)
            merge(arr, l, m , r)
        mergesort(nums, 0, len(nums))
        return nums