from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums) != Counter(set(nums))
        