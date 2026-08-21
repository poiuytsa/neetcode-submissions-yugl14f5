class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r=0,0     
        res=0   
        curr=0
        while r<len(nums):
            if nums[r]==1:
                curr+=1
                r+=1  
            else:
                while r<len(nums) and not nums[r]:
                    r+=1
                curr=0
                l=r
            res=max(res,curr)
        return res