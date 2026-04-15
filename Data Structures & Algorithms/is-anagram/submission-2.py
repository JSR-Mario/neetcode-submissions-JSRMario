from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int)

        if len(s) != len(t):
            return False

        for l in s:
            dictS[l] += 1
        
        for l in t:
            dictS[l] -= 1
            if dictS[l]<0:
                return False
        
        return True