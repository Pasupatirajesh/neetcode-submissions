class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True 
            if src not in adj:
                return False 
            
            temp = list(adj[src])
            for i, neighbor in enumerate(temp):
                adj[src].pop(i)
                res.append(neighbor)

                if dfs(neighbor): return True

                adj[src].insert(i, neighbor)
                res.pop()

            return False 
        
        dfs("JFK")
        return res             
