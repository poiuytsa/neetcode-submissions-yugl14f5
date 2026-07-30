class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxHeap=[-n for n in freq.values()]
        heapq.heapify(maxHeap)
        q=deque()           #store (freq,timeAtWhichAvailable)
        time=0
        while maxHeap or q:
            time+=1 

            if maxHeap:
                #in maxheap, proces and send to q, reduce freq by 1 
                curr=heapq.heappop(maxHeap)
                if curr+1<0:
                    q.append((curr+1, time+n))

            #ready to be moved from q to heap
            while q and q[0][1]==time:
                a,b=q.popleft()
                heapq.heappush(maxHeap,a)

        
        return time 