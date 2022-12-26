# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None

        val = 0
        if root1:
            val += root1.val
            left1 = root1.left
            right1 = root1.right
        else:
            left1 = None
            right1 = None

        if root2:
            left2 = root2.left
            val += root2.val
            right2 = root2.right
        else:
            left2 = None
            right2 = None

        return TreeNode(val, self.mergeTrees(left1, left2), self.mergeTrees(right1, right2))