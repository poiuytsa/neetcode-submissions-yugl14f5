class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry=0
        res=0
        MASK=0xFFFFFFFF
        a=a&MASK
        b=b&MASK 
        for i in range(32):
            lsb_a=a&1
            a=a>>1
            lsb_b=b&1
            b=b>>1

            xor=lsb_a^lsb_b^carry
            carry=1 if lsb_a+lsb_b+carry>=2 else 0

            res = (xor<<i)|res
        
        if res>=2**31:
            res-=2**32

        return res