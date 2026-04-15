class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n]+=1
        
        max_heap = []
        for key,v in counts.items():
            heapq.heappush(max_heap, (v,key))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
            
        return [v[1] for v in max_heap]
