class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for l in s:
            if l in brackets:
                stack.append(l)
            else:
                if not stack or brackets[stack.pop()] != l:
                    return False
        
        return not stack