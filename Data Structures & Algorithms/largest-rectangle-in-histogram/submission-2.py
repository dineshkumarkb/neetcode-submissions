class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # monotonic stack
        stack = []

        res = 0

        for index, height in enumerate(heights):

            start_index = index

            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                res = max(res, (index  - i) * h)
                start_index = i


            stack.append((start_index, height))

        for i, h in stack:
            res = max(res, (len(heights) - i) * h )

        return res