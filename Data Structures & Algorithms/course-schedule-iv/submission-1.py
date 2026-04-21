class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        prereqMap = {}

        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
            
            all_prereqs = set()
            for prereq in adj[crs]:
                all_prereqs |= dfs(prereq)
                all_prereqs.add(prereq)
            prereqMap[crs] = all_prereqs
            return prereqMap[crs]
        
        for crs in range(numCourses):
            dfs(crs)

            

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res