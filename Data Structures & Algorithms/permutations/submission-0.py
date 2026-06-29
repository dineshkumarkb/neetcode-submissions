class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, curr):

            if i == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(i + 1, curr)
                    curr.pop()

            return curr

        dfs(0, [])

        return res
        