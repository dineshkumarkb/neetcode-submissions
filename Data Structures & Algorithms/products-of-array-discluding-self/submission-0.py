class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # keep left and right pointers are 1
        left = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left * res[i]
            left *= nums[i]

        # traverse from right to left
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res 

        