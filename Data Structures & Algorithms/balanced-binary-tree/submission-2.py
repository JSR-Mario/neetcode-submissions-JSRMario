# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return True, 0
            lb, lh = height(root.left)
            rb, rh = height(root.right)
            balanced = lb and rb and abs(lh-rh)<=1
            return balanced, 1+max(lh,rh)

        balanced, _ = height(root)
        return balanced