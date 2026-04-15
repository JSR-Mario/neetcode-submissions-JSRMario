class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # solution mostly from neetcode
        n,m = len(s),len(t)
        if m>n:
            return ''

        letters_t = defaultdict(int)
        window    = defaultdict(int)

        for l in t:
            letters_t[l]+=1
        
        have,need = 0,len(letters_t)
        res, resLen = [-1,-1], float("infinity")

        l=0
        for r in range(n):
            letter_right = s[r]
            window[letter_right]+=1
            
            if letter_right in letters_t and window[letter_right]==letters_t[letter_right]:
                have +=1
            
            while have==need:
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen=r-l+1
            
                window[s[l]]-=1
                if s[l] in letters_t and window[s[l]]<letters_t[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ''