class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)

        def _backtracking(curr:list[int],left:list[int]):
            if len(left)==0:
                answer.append(curr.copy())
                return
            
            for i in range(len(left)):
                curr.append(left[i])
                _backtracking(curr,left[:i]+left[i+1:])
                curr.pop()

        _backtracking([],nums)
        return answer