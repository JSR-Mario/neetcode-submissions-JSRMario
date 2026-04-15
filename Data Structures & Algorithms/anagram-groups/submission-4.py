class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for s in strs:
            letters = [0]*26
            for l in s:
                letters[ord(l) - ord('a')] += 1
            groups[tuple(letters)].append(s)
        
        return list(groups.values())