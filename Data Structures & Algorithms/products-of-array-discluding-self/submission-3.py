class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        right = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]


        for j in range(len(nums) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]

        return res
        