class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most   = 0
        chars   = Counter()
        n       = len(s)
        longest = 0

        l,r=0,0
        while r<n:
            chars[s[r]]+=1
            most = max(most, chars[s[r]])

            while (r-l+1)-most>k:
                chars[s[l]]-=1
                l+=1

            r+=1
            longest = max(longest, r-l)
        
        return longest