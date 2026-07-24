class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Keep appending to a stack until we see an operand
        # On encountering an operand pop 2 recent values and apply the operand

        stack = []

        for t in tokens:

            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[-1]

