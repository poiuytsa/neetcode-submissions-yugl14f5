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
            memo[(i,left-coins[i])]=dfs(i,left-coins[i])
            memo[i+1,left]=dfs(i+1,left)
            return memo[(i,left-coins[i])]+memo[i+1,left]
        
        return dfs(0,amount)