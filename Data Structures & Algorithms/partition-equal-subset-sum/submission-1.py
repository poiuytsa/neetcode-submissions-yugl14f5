class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n=sum(nums)
        if sum_n%2:
            return False
        target=sum_n/2

        def dfs(i,subset):
            if i>=len(nums):
                return False
            if sum(subset)==target:
                return True
            subset.append(nums[i])
            if dfs(i+1,subset):
                return True
            subset.pop()
            if dfs(i+1,subset):
                return True
            return False
        
        return dfs(0,[])
        