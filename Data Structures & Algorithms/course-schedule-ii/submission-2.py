class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for i in range(numCourses)]
        indegree=[0]*numCourses

        for cor, pre in prerequisites:
            adj[pre].append(cor)
            indegree[cor]+=1
        
        q=deque()
        res=[]

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        done=0
        while q:
            temp=q.popleft()
            res.append(temp)
            done+=1 
            for nei in adj[temp]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        if done==numCourses:
            return res 
        else:
            return []