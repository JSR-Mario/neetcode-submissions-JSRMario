class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n]+=1
        max_heap = []
        for num,count in counts.items():
            heapq.heappush(max_heap,(count,num))

        return [num for _,num in heapq.nlargest(k, max_heap)]