class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t == "+":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele1 + ele2)
            elif t == "-":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele2 - ele1)
            elif t == "*":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(ele1 * ele2)
            elif t == "/":
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(int(ele2 / ele1))
            else:
                stack.append(int(t))

        return stack[-1]

        