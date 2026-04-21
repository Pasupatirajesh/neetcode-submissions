class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])
        
        # This builds your adjacency list to represent the graph/tree

        minHeap = []
        visit = set()
        visit.add(0)
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])
        
        # This builds the minHeap with the weight, source and neighbor of the source

        total_weight = 0
        while minHeap and len(visit) < n:
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            total_weight += weight

            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])
        

        
        return total_weight if len(visit) == n else -1