class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_in_sub   = set()
        length_longest = 0
        n              = len(s)

        r,l = 0,0
        while r<n:
            while s[r] in chars_in_sub:
                chars_in_sub.remove(s[l])
                l+=1
            chars_in_sub.add(s[r])
            r+=1
            length_longest = max(length_longest,r-l)
        
        return length_longest