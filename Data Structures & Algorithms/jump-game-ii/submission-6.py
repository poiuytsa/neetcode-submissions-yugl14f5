class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        res=0
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            r=max(l+nums[l],r+nums[r])            
            print(f"{l=} {r=}")
            res+=1
            if r>=len(nums)-1:
                return res 
            l=max(range(l,r+1), key=lambda x:nums[x])
            