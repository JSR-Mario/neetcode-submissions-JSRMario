class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        letters = [0]*26

        for l_s,l_t in zip(s,t):
            letters[ord(l_s)-ord('a')]+=1
            letters[ord(l_t)-ord('a')]-=1
        
        return all(l == 0 for l in letters)