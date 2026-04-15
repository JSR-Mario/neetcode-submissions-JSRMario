class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_list = [0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            letter_list[ord(s[i])-ord('a')]+=1
            letter_list[ord(t[i])-ord('a')]-=1
        return all(x==0 for x in letter_list)