class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        # busco un valor entre 1 y el max de piles
        maximo = max(piles)
        l,r=1,maximo

        while l<=r:
            k = l+(r-l)//2
            
            tiempo = 0
            for p in piles:
                tiempo += math.ceil(p/k)
            if tiempo <= h:
                r = k-1
            else:
                l=k+1
        return l