class Solution:
    def reverse(self, x: int) -> int:
        res=0
        isNegative=False
        if x<0:
            isNegative=True
            x=x*-1
        while x:   
            units=x%10 
            res=res*10 + units
            x=x//10
        
        if res>2**31 or res<-2**31: 
            return 0
        return res if not isNegative else -1*res