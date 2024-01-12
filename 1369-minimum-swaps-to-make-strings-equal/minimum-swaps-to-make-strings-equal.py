class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0; yx = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue 
            if s1[i] == 'x':
                xy+=1 
            else:
                yx+=1 
        
        if xy%2 != yx%2:
            return -1 
        
        if xy%2:
            return (xy+yx) // 2 +1

        return (xy+yx) //2 
        

        