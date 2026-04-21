class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for idx, (a, b) in enumerate(edges):
            prob = succProb[idx]
            adj[a].append((prob, b))
            adj[b].append((prob, a))
        
        maxHeap = [(-1, start_node)]
        visit = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node == end_node:
                return -prob
            if node in visit:
                    continue
            visit.add(node)
            
            for next_prob, next_node in adj[node]:
                if next_node not in visit:
                    heapq.heappush(maxHeap, (prob * next_prob, next_node))
        return 0.0

