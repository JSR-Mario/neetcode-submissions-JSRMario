class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def completable(num, seen):
            if num not in pre_dict:
                return True
            if num in seen:
                return False
            seen.add(num)
            for pre in pre_dict[num]:
                if not completable(pre,seen):
                    return False
            seen.remove(num)
            return True 

        pre_dict = defaultdict(list)
        for c,pre in prerequisites:
            pre_dict[c].append(pre)

        for i in range(numCourses):
            if i in pre_dict:
                if not completable(i,set()):
                    return False
        
        return True