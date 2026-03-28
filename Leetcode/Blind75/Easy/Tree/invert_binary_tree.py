from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if root is None, return None
        if not root:
            return None
        dummy = root
        # Swap the left and right children
        dummy.left, dummy.right = dummy.right, dummy.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(dummy.left)
        self.invertTree(dummy.right)
        
        return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(Solution().invertTree(root))