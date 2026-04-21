class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for course, preReq in prerequisites:
            graph[preReq].append(course)
            indegrees[course]+=1
        
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        taken = []

        while queue:
            course = queue.popleft()
            taken.append(course)
            for neighbor in graph[course]:
                indegrees[neighbor]-=1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return taken if len(taken) == numCourses else []