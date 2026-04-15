class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for p,s in zip(position,speed):
            stack.append((p,s))
        
        stack.sort(key=lambda x: x[0])

        answer = 1
        p,s = stack.pop()
        prev = (target-p)/s

        while stack:
            p,s = stack.pop()
            if ((target-p)/s)>prev:
                answer+=1
                prev=(target-p)/s
                
        return answer