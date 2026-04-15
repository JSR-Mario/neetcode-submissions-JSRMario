class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        
        l,r = 0,0
        seen = set(s[0])

        answer=0
        while r<len(s)-1:
            r+=1
            while s[r] in seen:
                answer = max(answer,r-l)
                seen.discard(s[l])
                l+=1
            seen.add(s[r])
        answer=max(answer,r-l+1)
        return answer