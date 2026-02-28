# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.result = 0
        def inOrder(node):
            if not node:
                return 0

            if k > self.count:
                inOrder(node.left)

            self.count += 1
            if k == self.count:
                self.result = node.val
                return
                
            if k > self.count:
                inOrder(node.right)
        
        inOrder(root)
        return self.result

        