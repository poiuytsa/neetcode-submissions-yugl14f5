class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs 
        # visited=set()
        # pre={}
        # for i in range(numCourses):
        #     pre[i]=[]
        # for cr,pr in prerequisites:
        #     pre[cr].append(pr)

        # def dfs(cr):
        #     if cr in visited:
        #         return False
        #     if pre[cr]==[]:
        #         return True
        #     visited.add(cr)
        #     for n in pre[cr]:
        #         if not dfs(n):
        #             return False 
        #     visited.remove(cr)
        #     pre[cr]=[]
        #     return True 
            

        # for cr,pr in prerequisites:
        #     if not dfs(cr):
        #         return False
        # return True



        #kahns algo 

        #uses index 
        adj=[[] for i in range(numCourses)]
        indegree=[0] * numCourses 
        for cor,pre in prerequisites:
            adj[cor].append(pre)
            indegree[pre]+=1
        
        q=deque()
        done=0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        while q:
            temp=q.popleft()
            done+=1 
            for nei in adj[temp]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return done==numCourses
        
