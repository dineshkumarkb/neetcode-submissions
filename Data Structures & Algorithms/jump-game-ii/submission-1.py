class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0

        l,r = 0, 0

        while r < len(nums) - 1:

            max_jump = 0

            for i in range(l, r + 1):
                max_jump = max(i + nums[i], max_jump)

            l = r + 1
            r = max_jump

            jumps += 1

        return jumps
        