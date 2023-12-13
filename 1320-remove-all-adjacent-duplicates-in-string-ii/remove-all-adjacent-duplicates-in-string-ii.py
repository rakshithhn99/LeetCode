class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        if len(s) < k:
            return s
        stack = [i for i in s[:k-1]]

        for i in range(k-1, len(s)):
            if len(stack) >= k-1 and stack[len(stack)-1] == s[i] and all(x == s[i] for x in stack[-(k-1):]):
                for i in range(k-1):
                    stack.pop()
                continue

            stack.append(s[i])

        return ''.join(stack)
                
            
            
