class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        zipped_list = list(zip(position, speed))

        zipped_list.sort(reverse= True)

        stack = []

        for pos, speed in zipped_list:

            time_taken = (target - pos) / speed

            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        