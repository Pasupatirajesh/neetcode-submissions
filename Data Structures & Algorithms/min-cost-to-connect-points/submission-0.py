class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        minHeap = [[0, 0]] #distance, pt_index
        adj = {}
        visit = set()

        for i in range(len(points)):
            adj[i] = []
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])        
                adj[j].append([dist, i])

        while minHeap and len(visit) < len(points):
            dist, i= heapq.heappop(minHeap)
            
            if i in visit:
                continue
            cost+=dist
            visit.add(i)
            for neiDist, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiDist, nei])



        return cost