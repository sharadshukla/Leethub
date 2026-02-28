# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.fgood = root.val

        def dfs(node):
            if not node:
                return
            
            if node.val >= self.fgood:
                self.good +=1
                self.fgood = node.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.good
