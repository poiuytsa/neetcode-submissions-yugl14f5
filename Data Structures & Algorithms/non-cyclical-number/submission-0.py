class Solution:
    def isHappy(self, n: int) -> bool:

        def sumOfSquares(x):
            sos=0
            while x:
                digit=x%10
                sos+=digit**2
                x=x//10
            return sos


        seen=set()
        while True:
            sos=sumOfSquares(n)
            if sos==1:
                return True
            if sos in seen:
                return False
            seen.add(sos)
            n=sos
