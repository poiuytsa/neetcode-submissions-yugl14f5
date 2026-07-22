class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        pre={}
        for i in range(numCourses):
            pre[i]=[]
        for cr,pr in prerequisites:
            pre[cr].append(pr)

        def dfs(cr):
            if cr in visited:
                return False
            if pre[cr]==[]:
                return True
            visited.add(cr)
            for n in pre[cr]:
                if not dfs(n):
                    return False 
            visited.remove(cr)
            pre[cr]=[]
            return True 
            

        for cr,pr in prerequisites:
            if not dfs(cr):
                return False
        return True