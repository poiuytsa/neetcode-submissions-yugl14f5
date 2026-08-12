class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,=0,0
        for n in nums:
            temp=max(a+n,b)
            a=b 
            b=temp
        return b