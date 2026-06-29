class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        res = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_idx, prev_t = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append((idx, t))

        return res
      