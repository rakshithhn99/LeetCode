class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat); n = len(mat[0])
        x = [0,0,-1,1]
        y = [1,-1,0,0]
        visited = {}; queue = []

        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    queue.append((i,j))
                    visited[(i,j)]=1

        res = [[0 for j in range(n)] for i in range(m)]
        
        while queue:
            front = queue.pop(0)
            row = front[0]; col = front[1]
            for i in range(4):
                new_row = row+x[i]; new_col = col+y[i]
                if new_row >=0 and new_row< m and new_col>=0 and new_col < n and not visited.get((new_row, new_col)):
                    queue.append((new_row, new_col))
                    res[new_row][new_col] = res[row][col] + 1
                    visited[(new_row, new_col)] = 1

        return res



        