class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        max_char_window = 0
        answer = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r],0)
            max_char_window = max(max_char_window,counter[s[r]])

            while (r-l+1)-max_char_window>k:
                counter[s[l]]-=1
                l+=1
            answer = max(answer, r-l+1)

        return answer        