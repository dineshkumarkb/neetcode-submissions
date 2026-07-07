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
                if stack:
                    if my_dict[stack[-1]] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                

        return stack == []


        