class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2

            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # this means we are in the left sorted array and search right
                l = mid + 1
            else:
                # this means we are in right sorted array and we should search left
                r = mid - 1

        return res

        