class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dirs=((0, 1),(1, 0),(0, -1),(-1, 0))
        minHeap=[(grid[0][0],0,0)]
        visited=set()
        
        while minHeap:
            max_d,r,c=heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r, c))

            if r==n-1 and c==n-1:
                return max_d
            
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if -1<nr<n and -1<nc<n and (nr,nc) not in visited:
                    new_d=max(max_d,grid[nr][nc])
                    heapq.heappush(minHeap,(new_d,nr,nc))
        return -1