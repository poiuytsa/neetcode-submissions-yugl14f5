class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,subset,currSum):
            if currSum>target or i>=len(nums):
                return 
            if currSum==target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i,subset,currSum+nums[i])

            subset.pop()
            dfs(i+1,subset,currSum)

        dfs(0,[],0)
        return res 