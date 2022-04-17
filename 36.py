class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(x+y)
            elif item == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif item == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(x*y)
            elif item == "/":
                y = stack.pop()
                x = stack.pop()
                if x * y < 0:
                    stack.append(-(abs(x)//abs(y)))
                else:
                    stack.append(x // y)
            else:
                stack.append(int(item))
        return stack[-1]