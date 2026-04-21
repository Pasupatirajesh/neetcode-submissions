class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue  = deque()
        minutes = 0
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count+=1
        if fresh_count == 0:
            return 0
        
        while queue:
            sz= len(queue)
            for _ in range(sz):
                r, c = queue.popleft()
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_count-=1

            minutes+=1
        return minutes -1 if fresh_count == 0 else -1



        