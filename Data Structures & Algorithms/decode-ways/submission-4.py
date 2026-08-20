class Solution:
    def numDecodings(self, s: str) -> int:
        #brute force
        # res=0
        # def dfs(i):
        #     if i==len(s):
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     if i<len(s)-1 and s[i] in ("1","2") and int(s[i+1]) in range(7):
        #         return dfs(i+1)+dfs(i+2)
        #     return dfs(i+1)
        # return dfs(0)

        res=0

        #index:number of ways to decode
        dp={len(s):1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            if i<len(s)-1 and 10<=int(s[i:i+2])<=26:
                dp[i]=dfs(i+1)+dfs(i+2)
            else:
                dp[i]=dfs(i+1)
            return dp[i]
        return dfs(0)