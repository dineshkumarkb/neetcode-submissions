class Solution:
    def isValid(self, s: str) -> bool:

        stack = []


        # have a dict for reference
        my_dict = {"{": "}", "[": "]", "(": ")"}

        # iterate thru the string
        for c in s:

            if c in my_dict:
                stack.append(c)
            else:
                if stack and my_dict[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return stack == []


        