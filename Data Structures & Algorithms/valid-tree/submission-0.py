class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(n)}
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        

