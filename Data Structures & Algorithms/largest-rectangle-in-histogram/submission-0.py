class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # have a monotonically increasing stack
        stack = []

        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                prev_idx, prev_height = stack.pop()
                res = max(res, (i - prev_idx) * prev_height)
                start = prev_idx
            stack.append((start, h))

        for i, h in stack:
            res = max(res, (len(heights) - i) * h)

        return res
        