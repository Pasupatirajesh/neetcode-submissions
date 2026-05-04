class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, req in prerequisites:
            adj[prereq].append(req)
        
        prereqMap= {}
        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
            
            prereqMap[crs] = set()
            for prereq in adj[crs]:
                prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(prereq)
            return prereqMap[crs]
            
        
        for crs in range(numCourses):
            dfs(crs)
        
        res= []
        for u, v in queries:
            res.append(v in prereqMap[u])
        return res