class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def _backtracking(curr:list[str],opened:int,closed:int):
            if opened==n and closed==n:
                answer.append(''.join(curr))

            if opened<n:
                curr.append('(')
                _backtracking(curr,opened+1,closed)
                curr.pop()
            
            if closed<opened:
                curr.append(')')
                _backtracking(curr,opened,closed+1)
                curr.pop()

        _backtracking([],0,0)

        return answer