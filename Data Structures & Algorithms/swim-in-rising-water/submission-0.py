class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Using Djikstra's with a minHeap (PQ)
        N = len(grid)
        visit = set()
        min_heap = [[grid[0][0], 0, 0]] #(time/max_height, r, c)
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        visit.add((0, 0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            # visit.add((r,c))
            if r == N -1 and c == N -1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(min_heap, [max(t, grid[neiR][neiC]), neiR, neiC])


