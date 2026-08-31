class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #number of ways for left
        memo=[-1]*(amount+1)

        def dfs(left):
            if left<0:
                return float('inf')
            if left==0:
                return 0

            if memo[left]!=-1:
                return memo[left]

            res=float('inf')

            for coin in coins:
                if left-coin>=0:
                    if memo[left-coin]!=-1:
                        res=min(res,1+memo[left-coin])
                    memo[left-coin]=dfs(left-coin)
                    res=min(res,1+memo[left-coin])
 
            return res

        ans=dfs(amount)
        return -1 if ans==float('inf') else ans