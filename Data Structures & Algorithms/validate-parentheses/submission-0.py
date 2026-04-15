class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for l in s:
            if l in brackets.values():
                stack.append(l)
            elif l in s:
                if not stack:
                    return False
                if stack.pop() != brackets[l]:
                    return False
        
        return not stack