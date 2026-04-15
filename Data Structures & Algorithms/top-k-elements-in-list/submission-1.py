class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        apears = [[] for _ in range(n)]

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        print(count)
        
        for e,f in count.items():
            apears[f-1].append(e)
        
        print(apears)
        
        answer = []
        for i in range(n-1,-1,-1):
            for n in apears[i]:
                answer.append(n)
                if len(answer)==k:
                    return answer