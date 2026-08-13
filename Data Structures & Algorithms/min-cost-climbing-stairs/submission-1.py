class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #brute force
        # def dfs(steps):
        #     if steps>=len(cost):
        #         return 0
        #     return cost[steps]+min(dfs(steps+1),dfs(steps+2))
        # return min(dfs(0),dfs(1))

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)