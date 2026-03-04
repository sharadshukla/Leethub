# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0
        # pre prder traversal
        def dfs(node, maxVal):

            if not node:
                return 0
            
            if node.val >= maxVal:
                self.count +=1
                maxVal = max(maxVal, node.val)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, float('-inf'))
        return self.count
            
































        # def dfs(node, maxVal):
        #     # Checking if node exists
        #     if not node:
        #         return 0
            
        #     # If value of node is greater than max value, then it is a good node
        #     # the good node count is assigned
        #     res = 1 if node.val >= maxVal else 0

        #     # Max value is chosen
        #     maxVal = max(maxVal, node.val)
            
        #     ## recursively the counter is incremented for all good nodes for
        #     # all the left subtrees
        #     res += dfs(node.left, maxVal)

        #     ## recursively the counter is incremented for all good nodes for
        #     # all the right subtrees
        #     res += dfs(node.right, maxVal)

        #     # returning the count value
        #     return res

        # # returning the result of dfs call
        # return dfs(root, float('-inf'))
