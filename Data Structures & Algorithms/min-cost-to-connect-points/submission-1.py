class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        minHeap = [[0, 0]]
        visit = set()
        n = len(points)
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j]) 
                adj[j].append([dist, i])
        
        while minHeap and len(visit) < n:
            cost, src = heapq.heappop(minHeap)
            if src in visit:
                continue
            visit.add(src)
            total_cost += cost
            for new_cost, neighbor in adj[src]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (new_cost, neighbor))

        return total_cost