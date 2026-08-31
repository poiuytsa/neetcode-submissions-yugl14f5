class Solution:
    def findMaxForm(self,strs:List[str],m:int,n:int)->int:
        memo={}
        def dfs(i,zeroes_left,ones_left):
            state=(i,zeroes_left,ones_left)
            if state in memo:
                return memo[state]
            if zeroes_left<0 or ones_left<0:
                return float('-inf')
            if i>=len(strs):
                return 0
            take=1+dfs(i+1,zeroes_left-strs[i].count('0'),ones_left-strs[i].count('1'))
            not_take=dfs(i+1,zeroes_left,ones_left)
            res=max(take,not_take)
            memo[state]=res
            return res
        return dfs(0,m,n)