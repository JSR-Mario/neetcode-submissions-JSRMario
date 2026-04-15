class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            s_list = [0]*26
            for l in s:
                s_list[ord(l)-ord('a')]+=1
            tuple_s = tuple(s_list)
            if tuple_s in groups:
                groups[tuple_s].append(s)
            else:
                groups[tuple_s] = [s]
        return [s for s in groups.values()]