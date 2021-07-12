# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, leftRoot, rightRoot):
        if leftRoot and rightRoot:
            if leftRoot.val == rightRoot.val and self.isMirror(leftRoot.left,rightRoot.right) and self.isMirror(leftRoot.right,rightRoot.left):
                return True
        return leftRoot==rightRoot
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self.isMirror(root.left,root.right)

    
        