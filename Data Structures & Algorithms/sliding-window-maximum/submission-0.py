class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        util = []
        for i in range(k):
            heapq.heappush(util,-nums[i])
        
        answer = []
        deleted = Counter()
        for i in range(k,len(nums)):
            answer.append(-util[0])
            heapq.heappush(util,-nums[i])
            deleted[nums[i-k]]+=1
            while deleted[-util[0]]>0:
                deleted[-util[0]]-=1 
                heapq.heappop(util)
        answer.append(-util[0])
        return answer