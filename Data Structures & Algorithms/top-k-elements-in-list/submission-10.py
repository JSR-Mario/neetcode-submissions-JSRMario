class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [val[0] for val in Counter(nums).most_common(k)]