class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        
        

        if numCourses == 1 and not prerequisites:
            return True
        if not prerequisites:
            return True

        adj_list = {i: [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            adj_list[course].append(preReq)
        
        def dfs(course):
            
            if course in path:
                return True
            if course in visited:
                return False
            path.add(course)
            for neighbor in adj_list[course]:
                if dfs(neighbor):
                    return True
            
            path.remove(course)
            visited.add(course)

            return False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
        

            