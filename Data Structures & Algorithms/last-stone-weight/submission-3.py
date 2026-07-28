class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-n for n in stones]
        heapq.heapify(maxHeap)
        if len(maxHeap)==1:
            return -maxHeap[0]
        while maxHeap:
            stone1=-heapq.heappop(maxHeap)
            stone2=-heapq.heappop(maxHeap)
            
            if stone1!=stone2:
                heapq.heappush(maxHeap,stone2-stone1)
            elif stone1==stone2 and len(maxHeap)==0:
                heapq.heappush(maxHeap,0)
            
            if len(maxHeap)==1:
                return -maxHeap[0]
            
            
