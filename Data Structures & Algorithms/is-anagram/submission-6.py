class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = defaultdict(int)
        for l in s:
            letters_s[l]+=1
        
        for l in t:
            if l not in letters_s:
                return False
            letters_s[l]-=1
            if letters_s[l]<0:
                return False

        return all(n==0 for n in letters_s.values())