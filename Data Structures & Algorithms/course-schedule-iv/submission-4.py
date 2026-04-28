class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, req in prerequisites:
            adj[req].append(prereq)
        
        res = []
        prereqMap = {}

        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
            
            visit = set()
            for prereq in adj[crs]:
                visit |= dfs(prereq)
                visit.add(prereq)
            prereqMap[crs] = visit
            return prereqMap[crs]
        
        for crs in range(numCourses):
            dfs(crs)
        
        for u , v in queries:
            res.append(u in prereqMap[v])
        return res 
