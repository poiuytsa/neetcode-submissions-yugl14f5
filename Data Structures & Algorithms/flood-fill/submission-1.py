class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        initialColor=image[sr][sc]
        dirs=((1,0),(-1,0),(0,1),(0,-1))
        ROWS=len(image)
        COLS=len(image[0])
        visited=set()

        #bfs 
        # q=deque()
        # q.append((sr,sc))

        # visited=set()
        # visited.add((sr,sc))

        # while q:
        #     r,c=q.popleft()
        #     image[r][c]=color
        #     for dr,dc in dirs:
        #         nr=dr+r
        #         nc=dc+c
        #         if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and image[nr][nc]==initialColor:
        #             visited.add((nr,nc))
        #             q.append((nr,nc))
                    
        # return image 


        #dfs 
        def dfs(r,c):
            visited.add((r,c))
            image[r][c]=color 
            for dr,dc in dirs:
                nr=dr+r 
                nc=dc+c 
                if 0<=nr<ROWS and 0<=nc<COLS and image[nr][nc]==initialColor and (nr,nc) not in visited:
                    dfs(nr,nc)
                
        dfs(sr,sc)
        return image


