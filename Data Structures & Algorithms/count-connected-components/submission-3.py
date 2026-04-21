class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        connected_components = 0
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node not in visited:
                visited.add(node)

                for neighbor in adj[node]:
                    if neighbor not in visited:
                        dfs(neighbor)

           
        
        for node in range(n):
            if node not in visited:
                connected_components+=1
                dfs(node)
        return connected_components
         