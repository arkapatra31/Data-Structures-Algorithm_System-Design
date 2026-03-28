# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# Ref - https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        if not root:
            return 0
        def calc_height(node: TreeNode):
            if not node:
                return 0
            left_height = calc_height(node.left)
            right_height = calc_height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        calc_height(root)
        return self.diameter

if __name__ == "__main__":
    # [10,9,20,null,null,15,7]
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().diameterOfBinaryTree(root))
        