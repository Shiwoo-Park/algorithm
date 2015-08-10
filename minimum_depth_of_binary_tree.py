# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root :
            return 0
        clevel = [root]
        depth = 1
        while len(clevel) != 0 :
            nlevel = list()
            for node in clevel :
                if self.isLeaf(node) :
                    return depth
                else :
                    if node.left :
                        nlevel.append(node.left)
                    if node.right :
                        nlevel.append(node.right)
            clevel = nlevel
            depth += 1

        return depth


    def isLeaf(self, node) :
        if node.left :
            return False
        if node.right :
            return False
        return True