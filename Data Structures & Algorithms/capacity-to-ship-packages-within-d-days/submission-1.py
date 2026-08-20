class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        def daysRequired(capacity):
            d=1
            curr=capacity
            for n in weights:
                curr-=n
                if curr<0:
                    d+=1
                    curr=capacity-n
            return d

        res=float('inf')
        while l<=r:
            m=(l+r)//2 

            temp=daysRequired(m)
            if temp>days:
                l=m+1
            else:
                res=min(res,m)
                r=m-1 

        return res

