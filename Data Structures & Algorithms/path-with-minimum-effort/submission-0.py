class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS=len(heights)
        COLS=len(heights[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))

        #effort,(cords)
        minHeap=[(0,(0,0))]
        visited=set()
        while minHeap:
            e,cords=heapq.heappop(minHeap)
            x,y=cords
            if (x,y) in visited:
                continue 
            visited.add(cords)
            if cords==(ROWS-1,COLS-1):
                return e
            for dr,dc in dirs:
                nr=dr+x 
                nc=dc+y 
                if nr>-1 and nr<ROWS and nc>-1 and nc<COLS and (nr,nc) not in visited:
                    new_e=max(e,abs(heights[x][y]-heights[nr][nc]))
                    heapq.heappush(minHeap,(new_e,(nr,nc)))
