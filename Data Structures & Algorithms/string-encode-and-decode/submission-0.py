class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result+=str(len(s))+'#'+s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s)-1:
            number=0
            while s[i]!='#':
                number= number*10+int(s[i])
                i+=1
            result.append(s[i+1:i+number+1])
            i+=1+number
        return result

