import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """O(n*log(k)),O(n)"""

        frequencies = defaultdict(int)
        for n in nums:
            frequencies[n]+=1
        
        min_heap = []
        for elem,freq in frequencies.items():
            heapq.heappush(min_heap,(freq,elem))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [e[1] for e in min_heap]