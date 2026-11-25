# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # init max path sum to root's val
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # calc max path sum through the node without split
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0) 
            res[0] = max(res[0], node.val + left_max + right_max)

            # calc max sum with split to return to the parent
            return node.val + max(left_max, right_max)

        dfs(root)

        return res[0]
