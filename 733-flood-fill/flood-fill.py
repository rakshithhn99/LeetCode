class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
       row = [-1, 1, 0, 0]
       col = [0, 0, -1, 1] 
       m = len(image); n = len(image[0]); queue = []; sourceVal = image[sr][sc]
       queue.append((sr,sc))

       while queue:
           index_tuple = queue.pop(0)
           sr = index_tuple[0]; sc = index_tuple[1]
           if image[sr][sc] == color:
               continue 

           image[sr][sc] = color
           for i in range(4):
               new_sr = sr+row[i]
               new_sc = sc+col[i]
               if new_sr>=0 and new_sr<m and new_sc>=0 and new_sc<n and image[new_sr][new_sc] == sourceVal:
                   queue.append((new_sr,new_sc))
        
       return image
            

           

        