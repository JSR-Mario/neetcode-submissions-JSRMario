class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([
            str(len(s)) + '#' + s for s in strs 
        ])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            keyword_index = s.find('#',i)
            length = int(s[i:keyword_index])
            res.append(s[keyword_index+1:keyword_index+1+length])
            i = keyword_index+length+1
        
        return res