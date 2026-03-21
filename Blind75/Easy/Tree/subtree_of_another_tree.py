from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If root doesn't exist, return False
        if not root:
            return False
        # If root and subRoot are identical, return True
        if self.__isIdentical(root,subRoot):
            return True
        # If root and subRoot are not identical,
        # check if the left or right subtree of root is identical to subRoot
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def __isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        return (
            root.val == subRoot.val and 
            self.__isIdentical(root.left,subRoot.left) and 
            self.__isIdentical(root.right,subRoot.right)
        )

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    #root.left.right.left = TreeNode(0)
    
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(Solution().isSubtree(root, subRoot))