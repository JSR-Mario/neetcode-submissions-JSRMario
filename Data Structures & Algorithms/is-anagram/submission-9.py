class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26

        if len(s)!=len(t):
            return False
        
        n = len(s)

        for i in range(n):
            chars[ord(s[i])-ord('a')] += 1
            chars[ord(t[i])-ord('a')] -= 1
        
        for i in range(26):
            if chars[i]!=0:
                return False
        
        return True 