class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # bfs, where the adjacent nodes are strings that can be reache with 1 change 

        q=deque()
        q.append('0000')
        dead=set(deadends)
        visited=set()
        visited.add('0000')

        if '0000' in dead:
            return -1

        res=0
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==target:
                    return res
                #generate all combs    
                arr=list(map(int,curr))
                for i in range(4):
                    temp=arr.copy()
                    temp[i]=temp[i]+1 if temp[i]!=9 else 0
                    if "".join(map(str,temp)) not in dead and "".join(map(str,temp)) not in visited:
                        q.append("".join(map(str,temp)))
                        visited.add("".join(map(str,temp)))
                    temp=arr.copy()
                    temp[i]=temp[i]-1 if temp[i]!=0 else 9
                    if "".join(map(str,temp)) not in dead and "".join(map(str,temp)) not in visited:
                        q.append("".join(map(str,temp)))
                        visited.add("".join(map(str,temp)))
            if q:
                res+=1 
        return -1