class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {
            ')':'(' ,
            '}':'{' ,
            ']':'[' ,
        }

        stack = deque()

        for i in range(len(s)):
            if s[i] in valid:
                if not stack or stack.pop() != valid[s[i]]:
                    return False
            else:
                stack.append(s[i])
        
        return not stack