class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        zipped_list = list(zip(position, speed))

        zipped_list.sort(reverse=True)

        for p, s in zipped_list:

            time  = (target - p) / s

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)
        