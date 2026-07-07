class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        my_dict = {"{": "}", "[": "]", "(": ")"}

        stack = []

        for c in s:
            if c in my_dict:
                stack.append(c)
            else:
                if not stack or my_dict[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
                

        return stack == []


        