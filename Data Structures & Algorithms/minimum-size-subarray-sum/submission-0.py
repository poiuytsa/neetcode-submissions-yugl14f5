class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,curr_sum=0,0,0
        minL=float('inf')
        while r<len(nums):
            curr_sum+=nums[r]
            while curr_sum>=target:
                minL=min(minL,r-l+1)
                curr_sum-=nums[l]
                l+=1
            r+=1
        return minL if minL<float('inf') else 0