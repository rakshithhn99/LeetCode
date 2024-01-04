class Solution:
    def isValid(self, s: str) -> bool:
        inputString = list(s)
        valid = ['(', '[', '{']
        stack = []
        print(inputString)
        for char in inputString:
            if char in valid:
                stack.append(char)
                continue
                
            if not len(stack):
                return False

            if char == ')' and stack[len(stack)-1] != '(':
                return False 
            if char == ']' and stack[len(stack)-1] != '[':
                return False 
            if char == '}' and stack[len(stack)-1] != '{':
                return False 
            
            stack.pop()
        
        if len(stack):
            return False 
        
        return True


            

        