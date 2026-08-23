class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # #if 1 set bit 
        # count=0
        # while n:
        #     print(n&1)
        #     count+=1 if n&1 else 0
        #     if count>1:
        #         return False
        #     n=n>>1 
        # #count shouldnt be 0 either 
        # return True if count else False 

        return True if not n&(n-1) and n!=0 else False