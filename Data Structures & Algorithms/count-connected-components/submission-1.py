class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected_components = 0
        visited = set()

        adj_list = {i:[] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                connected_components+=1
        return connected_components

                
