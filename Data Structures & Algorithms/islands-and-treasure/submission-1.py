class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((0, r, c))
        while queue:
            count, r, c = queue.popleft()
            neighbors = [(0, 1), (0,-1), (-1, 0), (1, 0)]
            for dr, dc in neighbors:
                nr, nc = r + dr, c+ dc

                if nr < 0 or nr>= ROWS or nc < 0 or nc >=COLS or grid[nr][nc] <= count+1:
                    continue

                grid[nr][nc] = count+1
                queue.append((count+1, nr, nc))        