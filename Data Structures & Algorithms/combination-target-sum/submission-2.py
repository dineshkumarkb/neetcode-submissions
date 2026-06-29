class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, total):
            if i < len(nums) and total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            total += nums[i]
            dfs(i, curr, total)

            curr.pop()
            total -= nums[i]
            dfs(i + 1, curr, total)

            return curr

        dfs(0, [], 0)

        return res
        