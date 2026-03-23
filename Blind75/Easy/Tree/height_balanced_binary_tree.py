from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

if __name__ == "__main__":
    # [1,2,2,3,3,null,null,4,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(Solution().isBalanced(root))
        
            
            
        