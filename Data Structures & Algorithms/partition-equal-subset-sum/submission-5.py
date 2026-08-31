class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n=sum(nums)
        if sum_n%2:
            return False
        target=sum_n//2

        # def dfs(i,subset):
        #     if i>=len(nums):
        #         return False
        #     if sum(subset)==target:
        #         return True
        #     subset.append(nums[i])
        #     if dfs(i+1,subset):
        #         return True
        #     subset.pop()
        #     if dfs(i+1,subset):
        #         return True
        #     return False
        
        # return dfs(0,[])

        #(i,curr_sum):True/False
        memo={}

        def dfs(i,curr_sum):
            if i>=len(nums):
                return curr_sum==target
            if curr_sum==target:
                return True
            if curr_sum>target:
                return False
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            memo[(i,curr_sum)]=dfs(i+1,curr_sum) or dfs(i+1,curr_sum+nums[i])
            return memo[(i,curr_sum)]

        if dfs(0,0):
            return True
            
        return False
        