class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(
            str(len(s)) + '#' + s for s in strs
        )

    def decode(self, s: str) -> List[str]:
        if not s: return []
        answer = []
        print(s)

        i=0
        while i < len(s):
            j = s[i:].find('#')+i
            length = int(s[i:j])
            answer.append(s[j+1:j+length+1])
            i = j+length+1
        return answer