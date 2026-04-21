class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
           
        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                for prereq in adj[course]:
                    prereqMap[course] |= dfs(prereq)
                prereqMap[course].add(course)
            return prereqMap[course]
        
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        answer = []
        for u, v in queries:
                answer.append(u in prereqMap[v])
        return answer