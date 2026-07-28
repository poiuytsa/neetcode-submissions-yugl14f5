class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        # #no need to sqrt
        # maxHeap=[(-(n[0]**2+n[1]**2),(n[0],n[1])) for n in points] 
        # heapq.heapify(maxHeap)
        # while len(maxHeap)>k:
        #     heapq.heappop(maxHeap)
        
        # res=[]

        # for i in range(k):
        #     res.append(list(maxHeap[i][1]))

        # return res


        maxHeap,res=[],[]

        for n in points:
            dist=n[0]**2+n[1]**2
            heapq.heappush(maxHeap,(-dist,(n[0],n[1])))
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        
        while maxHeap:
            res.append(list(heapq.heappop(maxHeap)[1]))

        return res
