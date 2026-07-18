class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subset=[]
        def dfs(op,clo):
            if len(subset)==2*n and op==clo:
                res.append("".join(subset))
                return 
            if op<clo or op>n:
                return 

            subset.append('(')
            dfs(op+1,clo)
            subset.pop()
            subset.append(')')
            dfs(op,clo+1)
            subset.pop()

        dfs(0,0)
        return res

