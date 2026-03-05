# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(lp, rp):
            if lp > rp:
                return None
            
            mid = (lp+rp) // 2
            root = TreeNode(nums[mid])
            root.left = BST(lp, mid-1)
            root.right = BST(mid+1, rp)
            return root

        return BST(0, len(nums) - 1)
        