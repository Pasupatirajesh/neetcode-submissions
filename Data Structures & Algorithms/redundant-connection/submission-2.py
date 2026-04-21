class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(len(edges)+1)}

        def dfs(parent, node):
            if visit[node]:
                return True
            
            visit[node] = True
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if dfs(node, neighbor):
                    return True
            return False
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            visit = [False] * (len(edges)+1)

            if dfs(-1, u):
                return [u, v]
        return []
