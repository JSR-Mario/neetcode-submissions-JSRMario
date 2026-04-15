from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        util = defaultdict(list)

        for w in strs:
            letters = [0]*26
            for l in w:
                letters[ord(l)-96] +=1
            
            util[tuple(letters)].append(w)
        
        return [l for l in util.values()]   