class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        #adjacency list 
        for u,v,w in times:
            adj[u].append((v,w))

        minHeap=[]
        heapq.heappush(minHeap,(0,k))
        visited=set()
        time=0    
        
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visited:
                continue
            time=max(time,w1)
            visited.add(n1)
            for nei,w in adj[n1]:
                if nei not in visited:
                    heapq.heappush(minHeap,(w+w1,nei))

        return time if len(visited)==n else -1