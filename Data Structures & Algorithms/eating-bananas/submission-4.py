import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(k):
            hours=0
            for n in piles:
                hours+=math.ceil(n/k)
            if hours<=h:
                return True

        l=1
        r=max(piles)
        minPossible=max(piles)
        while l<=r:
            k=(l+r)//2
            if isValid(k):
                minPossible=k
                r=k-1
            else:
                l=k+1
        return minPossible 
