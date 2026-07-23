class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        res = 0

        for index, height in enumerate(heights):

            # remember the prev index to extend back
            start = index

            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                res = max(res, (index - i) * h)
                start = i

            stack.append((start, height))

        for i, h in stack:
            res = max(res, (len(heights) - i) * h)

        return res
        