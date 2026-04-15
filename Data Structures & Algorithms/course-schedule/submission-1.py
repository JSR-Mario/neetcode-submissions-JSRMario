class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [set() for _ in range(numCourses)]

        for u,v in prerequisites:
            edges[u].add(v)

        def dfs(u:int,seen:set()):
            seen.add(u)
            if edges[u] & seen:
                return True
            
            for req in edges[u]:
                if dfs(req,seen.copy()):
                    return True
        
        for i in range(numCourses):
            if dfs(i,set()):
                return False
        
        return True
