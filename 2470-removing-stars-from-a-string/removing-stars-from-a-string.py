class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == '*' and stack[len(stack)-1] != '*':
                stack.pop()
                continue
            
            stack.append(i)
        
        return ''.join(stack)
            
            
     
            
        