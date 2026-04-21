class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((0, r, c))
        
        
        while queue:
            count, r, c = queue.popleft()
            neighbors = [(0,1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc

                if nr < 0  or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] <= count +1:
                    continue

                grid[nr][nc] = count+1
                queue.append((count+1, nr, nc))
