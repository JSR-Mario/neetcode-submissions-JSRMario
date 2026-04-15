class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        letters_s = [0]*26
        letters_t = [0]*26
    
        for i in range(len(s)):
            letters_s[ord(s[i]) - ord('a')]+=1
            letters_t[ord(t[i]) - ord('a')]+=1
        
        return letters_s==letters_t