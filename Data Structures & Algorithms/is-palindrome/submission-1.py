class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l,r=0,len(s)-1
        print(s)
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[r]!=s[l]:
                return False
            l+=1
            r-=1
        return True 