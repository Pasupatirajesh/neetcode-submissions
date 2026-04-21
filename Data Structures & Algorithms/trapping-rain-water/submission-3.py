class Solution:
    def trap(self, height: List[int]) -> int:
        prearr, suarr, res = 0, 0, 0
        prefix, suffix = [], []

        for i in range(len(height)):
            prearr = max(prearr, height[i])
            prefix.append(prearr)
        
        for i in range(len(height)-1, -1, -1):
            suarr = max(suarr, height[i])
            suffix.append(suarr)
        
        suffix.reverse()

        for i in range(len(height)):
            res+= min(prefix[i], suffix[i]) - height[i]
        
        return res 