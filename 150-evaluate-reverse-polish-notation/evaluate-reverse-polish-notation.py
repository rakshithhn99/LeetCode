class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:

            if token not in operands:
                stack.append(int(token))
                continue

            second = stack.pop()
            first = stack.pop()

            if token == '+':
                res = second+first
            elif token == '-':
                res = first - second 
            elif token == '*':
                res = first*second 
            else:
                val = 1
                if (first < 0 and second >= 0) or (first >=0 and second < 0) :
                    val = -1 
                res = abs(first) // abs(second)
                res*=val
            
            print(res)

            stack.append(res)

        return stack.pop()


        