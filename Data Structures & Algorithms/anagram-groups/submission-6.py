class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            s_letters = [0]*26
            for l in s:
                s_letters[ord(l)-ord('a')] += 1
            anagram_dict[tuple(s_letters)].append(s)
        
        return [ana for ana in anagram_dict.values()]