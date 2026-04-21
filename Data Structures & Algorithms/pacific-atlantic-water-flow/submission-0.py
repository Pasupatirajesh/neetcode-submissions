class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # res = []
        ahs = set()
        phs = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, hs, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in hs:
                return
            if heights[r][c] < prev_height:
                return        
            hs.add((r, c))

            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in neighbors:
                dfs(r+dr, c+ dc, hs, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, phs, heights[0][c])
            dfs(rows-1, c, ahs, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, phs, heights[r][0])
            dfs(r, cols-1, ahs, heights[r][cols-1])
        res = [[r,c] for r, c in ahs & phs]
        return res