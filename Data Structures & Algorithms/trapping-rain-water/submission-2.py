class Solution:
    def trap(self, height: List[int]) -> int:
        psum = 0
        ssum = 0
        prearr = []
        suarr = []
        for i in range(len(height)):
            psum = max(psum, height[i])
            prearr.append(psum)

        for i in range(len(height)-1, -1, -1):
            ssum = max(ssum, height[i])
            suarr.append(ssum)
        suarr.reverse()
        
        res = 0
        for i in range(len(height)):
            res += min(prearr[i], suarr[i]) - height[i]
        return res
            
