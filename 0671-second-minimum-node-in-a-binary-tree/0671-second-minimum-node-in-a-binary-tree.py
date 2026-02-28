# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min1 = root.val
        self.min2 = float('inf')

        def dfs(node):
            if not node:
                return -1
            if self.min1 < node.val < self.min2:
                self.min2 = node.val
                return self.min2
            elif self.min1 == node.val:
                dfs(node.left)
                dfs(node.right)
            
        dfs(root)
        return self.min2 if self.min2 < float('inf') else -1

        