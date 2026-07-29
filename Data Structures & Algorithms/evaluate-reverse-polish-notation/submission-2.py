class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 4 operations
        # You need to iterate from beginning of stack, how? Convert stack to deque + int
        # when popping from left, check if it's arithmetic or a number.
        # If arithmetic, maintain a stack which contains only number and until that point pop and have a result.
        # Store the result back in the stack.
        # Return result in stack.
        result = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                result.append(int(token))
            elif token == "+":
                right = result.pop()
                left = result.pop()
                res = left + right
                result.append(res)
            elif token == "-":
                right = result.pop()
                left = result.pop()
                res = left - right
                result.append(res)
            elif token == "*":
                right = result.pop()
                left = result.pop()
                res = left * right
                result.append(res)
            elif token == "/":
                right = result.pop()
                left = float(result.pop())
                res = int(left / right)
                result.append(res)
        return result.pop()


            
                

        

        