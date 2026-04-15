class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]

        answer = [0]*len(temperatures)

        for i,t in enumerate(temperatures[1:],1):
            while stack and t>temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx]=i-idx
            stack.append(i)


        return answer