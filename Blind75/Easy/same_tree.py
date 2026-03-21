from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        else:
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(
                        p.right, q.right
                    )


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(None)
    print(Solution().isSameTree(root1, root2))
