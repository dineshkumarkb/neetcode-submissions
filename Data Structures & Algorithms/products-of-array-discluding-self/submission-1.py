class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # keep left and right pointers are 1
        left = 1
        res = []

        for i in range(len(nums)):
            res.append(left)
            left *= nums[i]

        # traverse from right to left
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res 

        