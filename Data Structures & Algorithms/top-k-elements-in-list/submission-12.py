import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        mostFreq = []

        for key,v in counts.items():
            heapq.heappush(mostFreq, (v,key))
            if len(mostFreq) > k:
                heapq.heappop(mostFreq)
            
        return [n[1] for n in mostFreq]

        