# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):

            if not node:
                return True

            if left >= node.val or right <= node.val:
                return False

            left_node = dfs(node.left, left, node.val)
            right_node = dfs(node.right, node.val, right)

            return left_node and right_node

        return dfs(root, float("-inf"), float("inf"))
        