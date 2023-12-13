class Solution:
    def removeDuplicates(self, s: str) -> str:

        if len(s) == 1 or not s:
            return s

        stack = [s[0]]
        for i in range(1, len(s)):
            if stack:
                if stack[len(stack)-1] == s[i]:
                    stack.pop()
                    continue
            stack.append(s[i])
        
        return ''.join(stack)
        

        