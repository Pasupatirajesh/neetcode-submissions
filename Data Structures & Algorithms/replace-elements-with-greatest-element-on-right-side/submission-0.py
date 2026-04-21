class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        greatest = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            res[i] = greatest
            greatest = max(greatest, arr[i])
        return res


        

