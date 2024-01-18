class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_islands = 0
        visited = {}; x = [-1,1,0,0]; y = [0,0,1,-1]
        m = len(grid); n = len(grid[0])
        queue = []

        def dfs(queue, visited, m, n, x, y,grid):
            while queue:
                front = queue.pop(0)
                row = front[0]; col = front[1]
                for i in range(4):
                    new_row = row + x[i]
                    new_col = col + y[i]
                    
                    if new_row>=0 and new_row<m and new_col>=0 and new_col<n and grid[new_row][new_col] == '1' and not visited.get((new_row,new_col)):
                        queue.append((new_row,new_col))
                        visited[(new_row, new_col)] = 1       


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited.get((i,j)):
                    queue.append((i,j))
                    visited[(i,j)]=1
                    dfs(queue,visited,m,n,x,y,grid)
                    no_islands+=1

        return no_islands



        