class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i:int, j:int):
            for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                newi=i+di
                newj=j+dj
                if 0 <= newi and newi<h and 0<=newj and newj<w and grid[newi][newj] == "1":
                    grid[newi][newj]="2"
                    dfs(newi, newj)
                    
        h=len(grid)
        w=len(grid[0])
        count=0
        for i in range(h):
            for j in range(w):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i, j)
        return count
    
    def numIslandsFast(self, grid: List[List[str]]) -> int:
        d=deque([])

        def dfs(i:int, j:int):
            d.append((i, j))
            while d:
                i, j = d.popleft()
                for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                    newi=i+di
                    newj=j+dj
                    if 0 <= newi and newi<h and 0<=newj and newj<w and grid[newi][newj] == "1":
                        grid[newi][newj]="2"
                        d.append((newi, newj))


        h=len(grid)
        w=len(grid[0])
        count=0
        for i in range(h):
            for j in range(w):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i, j)
        return count

        

        