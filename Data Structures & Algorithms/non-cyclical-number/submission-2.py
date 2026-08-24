class Solution:
    def isHappy(self, n: int) -> bool:

        def sumOfSquares(x):
            sos=0
            while x:
                digit=x%10
                sos+=digit**2
                x=x//10
            return sos

        #O(n) space complexity
        # seen=set()
        # while True:
        #     sos=sumOfSquares(n)
        #     if sos==1:
        #         return True
        #     if sos in seen:
        #         return False
        #     seen.add(sos)
        #     n=sos
    
        #O(1) space complexity - floyds algo 

        slow=n
        fast=sumOfSquares(n)
        while slow!=fast:
            slow=sumOfSquares(slow)
            fast=sumOfSquares(fast)
            fast=sumOfSquares(fast)
        #return True if fast==1 else False
        return True if slow==1 else False
