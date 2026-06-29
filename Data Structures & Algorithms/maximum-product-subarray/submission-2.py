class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        min_product, max_product = 1, 1

        res = nums[0]

        for n in nums:
            temp = max_product * n
            max_product = max(n, max_product * n, min_product * n)
            min_product = min(n, temp, min_product * n)

            res = max(res, max_product)


        return res
        