from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int)

        for l in s:
            dictS[l] += 1
        
        for l in t:
            if l not in dictS or dictS[l]==0:
                return False
            dictS[l] -= 1
        
        return all(i==0 for i in dictS.values())