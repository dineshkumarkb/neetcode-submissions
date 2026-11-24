# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # init max value
        res = [root.val]

        def dfs(root):

            if not root:
                return 0

            # compute max val without split
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val + left_max + right_max)

            # compute max value and return with split
            return root.val + max(left_max, right_max)

        dfs(root)

        return res[0]


        