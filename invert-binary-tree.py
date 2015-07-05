# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.reverse(root)
        return root

    def reverse(self, root):
        if not root:
            return
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.reverse(root.left)
        self.reverse(root.right)