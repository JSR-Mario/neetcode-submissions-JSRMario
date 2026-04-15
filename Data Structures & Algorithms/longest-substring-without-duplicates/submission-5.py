class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0

        longest = 1

        l,r = 0,0
        window = set()
        while r<n-1:
            window.add(s[r])
            r+=1
            longest = max(longest, r-l)
            while s[r] in window:
                window.remove(s[l])
                l+=1
            
        return max(longest, r-l+1)