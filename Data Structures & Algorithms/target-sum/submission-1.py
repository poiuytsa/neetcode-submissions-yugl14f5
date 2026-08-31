class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        #(i,curr_sum):no_of_ways
        memo={}
        def dfs(i,curr_sum):
            if i>=len(nums):
                if curr_sum==target:
                    return 1
                return 0
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            memo[(i,curr_sum)]=dfs(i+1,curr_sum+nums[i])+dfs(i+1,curr_sum-nums[i]) 
            return memo[(i,curr_sum)]
        return dfs(0,0)