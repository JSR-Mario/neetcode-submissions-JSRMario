class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            req[u].append(v)
        
        state = [0]*numCourses

        def cycle(course:int):
            if state[course]==1:
                return True
            
            if state[course]==2:
                return False

            state[course]=1

            for pre in req[course]:
                if cycle(pre):
                    return True
            
            state[course]=2
            
            return False 


        for i in range(numCourses):
            if cycle(i):
                return False
        
        return True