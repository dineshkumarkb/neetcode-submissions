class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotonically decreasing stack
        # cz we need to find increasing temperature

        stack = []

        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append((idx, temp))

        return res
