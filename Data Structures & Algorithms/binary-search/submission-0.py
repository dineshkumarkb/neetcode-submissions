class Solution:
    def search(self, nums: List[int], target: int) -> int:

        res = -1

        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):

            mid = (l + r) // 2

            pivot = nums[mid]

            if pivot == target:
                return mid
            elif pivot < target:
                l += 1
            elif pivot > target:
                r -= 1
            else:
                return -1

        return res
        