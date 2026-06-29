class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set(nums)

        res = 0

        for n in nums:
            if n - 1 not in my_set:
                start = n
                length = 1
                while start + length in my_set:
                    length += 1
                res = max(res, length)

        return res



            
        