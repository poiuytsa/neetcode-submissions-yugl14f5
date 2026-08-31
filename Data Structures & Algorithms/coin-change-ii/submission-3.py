class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #(i,left)-> number of ways to reach amount
        memo={}

        def dfs(i,left):
            if i>=len(coins) or left<0:
                return 0
            if left==0:
                return 1
            if (i,left) in memo:
                return memo[(i,left)]
            memo[(i,left)]=dfs(i,left-coins[i])+dfs(i+1,left)
            return memo[(i,left)]
        
        return dfs(0,amount)