class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        visited = {}; queue = []; x = [1,-1,0,0]; y = [0,0,-1,1]

        def multi_dfs(queue, visited, x, y, m, n, grid):
            minute_elapse = 0
            while queue:
                front = queue.pop(0); temp = []
                for val in front:
                    row = val[0]; col = val[1]
                    for i in range(4):
                        new_row = row + x[i]; new_col = col + y[i]
                        if new_row >=0 and new_row<m and new_col>=0 and new_col<n and grid[new_row][new_col] == 1 and not visited.get((new_row, new_col)):
                            temp.append((new_row, new_col))
                            visited[(new_row, new_col)] = 1

                if temp:
                    queue.append(temp)
                    minute_elapse+=1
            return minute_elapse


        temp = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    temp.append((i,j))
        if temp:
            queue.append(temp)
        minute_elapse = multi_dfs(queue,visited, x, y, m, n, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited.get((i,j)):
                    return -1 

        return minute_elapse
                    