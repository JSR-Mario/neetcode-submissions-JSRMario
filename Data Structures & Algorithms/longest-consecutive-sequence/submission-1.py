class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numeros = set(nums)

        longest = 1
        for e in nums:
            curr = 1
            while e+1 in numeros:
                curr +=1
                e += 1
            longest = max(longest, curr)

        return longest