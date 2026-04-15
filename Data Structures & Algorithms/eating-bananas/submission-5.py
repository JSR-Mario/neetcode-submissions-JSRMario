from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on k in [1, max(piles)]
        left, right = 1, max(piles)

        def can_finish(k: int) -> bool:
            hours = 0
            for pile in piles:
                # ceil(pile / k)
                hours += (pile + k - 1) // k
                if hours > h:  # early exit
                    return False
            return hours <= h

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
