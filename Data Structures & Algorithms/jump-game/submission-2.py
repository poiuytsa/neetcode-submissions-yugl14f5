class Solution:
    def canJump(self, nums: List[int]) -> bool:
        aim=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=aim:
                aim=i

        return aim==0
