class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res=1
        # if x==1:
        #     return 1
        # if x==-1:
        #     return x if n%2 else -x
        # for _ in range(abs(n)):
        #     res*=x 
        # return res if n>0 else 1/res

        def rec(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            res=rec(x,n//2)
            return res*res*x if n%2 else res*res 

        res=rec(x,abs(n))
        return res if n>0 else 1/res