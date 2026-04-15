from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        util = c.most_common(k)
        return [v[0] for v in util]
        