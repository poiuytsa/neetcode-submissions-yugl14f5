class Solution:
    def climbStairs(self, n: int) -> int:

        #brute force 
        # def dfs(curr_steps):
        #     if curr_steps==n:
        #         return 1
        #     if curr_steps>n:
        #         return 0 
        #     return dfs(curr_steps+1)+dfs(curr_steps+2)

        # return dfs(0)


        #top down approach 
        #cache the value for dfs(i) for i
        dp=[-1]*n
        def dfs(curr_steps):
            if curr_steps==n:
                return 1
            if curr_steps>n:
                return 0
            if dp[curr_steps]!=-1:
                return dp[curr_steps]
            dp[curr_steps]=dfs(curr_steps+1)+dfs(curr_steps+2)
            return dp[curr_steps]
        return dfs(0)



