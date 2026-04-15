class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1001
        curr_sum = 0
        for n in nums:
            curr_sum += n
            max_sum = max(max_sum,curr_sum)
            curr_sum = 0 if curr_sum<0 else curr_sum
        return max_sum