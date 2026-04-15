class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        
        l,r=0,0
        longest=0

        seen = set()
        while r<len(s):
            if s[r] in seen:
                longest = max(longest,r-l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            r+=1
        
        return max(longest,r-l)