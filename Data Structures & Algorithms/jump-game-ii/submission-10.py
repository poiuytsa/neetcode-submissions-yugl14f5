class Solution:
    def jump(self, nums: List[int]) -> int:
        # l,r=0,0
        # res=0
        # if len(nums)==1:
        #     return 0
        # for i in range(len(nums)):
        #     r=max(l+nums[l],r+nums[r])            
        #     print(f"{l=} {r=}")
        #     res+=1
        #     if r>=len(nums)-1:
        #         return res 
        #     l=max(range(l,r+1), key=lambda x:nums[x])


        l,r,res=0,0,0
        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            res+=1
            r=farthest
            
        return res 
            