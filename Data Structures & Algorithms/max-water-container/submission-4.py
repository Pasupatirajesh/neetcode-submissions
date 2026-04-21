class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxres, res = 0,0
        j, k = 0, len(heights)-1
        while j < k:
            res = (k-j) * min(heights[j], heights[k])
            maxres = max(maxres, res)
            if heights[j] <= heights[k]:
                j+=1
            else:
                k-=1
        return maxres



