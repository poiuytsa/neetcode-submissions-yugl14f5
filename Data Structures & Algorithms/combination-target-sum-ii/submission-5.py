class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,subset,currSum):
            if currSum==target:
                res.append(subset.copy())
                return
            if i>=len(candidates) or currSum>target:
                return 

            subset.append(candidates[i])
            dfs(i+1,subset,currSum+candidates[i])

            subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,subset,currSum)

        dfs(0,[],0)
        return res