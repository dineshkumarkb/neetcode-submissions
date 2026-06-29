class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        res = []

        for n in nums:
            res.append(left)
            left *= n

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
        