class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        result = []
        for num, count in counts.items():
            heapq.heappush(result, (count,num))
            if len(result)>k:
                heapq.heappop(result)

        return [num for _,num in result]        