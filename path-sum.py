# https://leetcode.com/problems/path-sum/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum) :
        if root :
            return self.hasSum(root, root.val, sum)
        return False

    def isLeaf(self, node) :
        if node.left :
            return False
        if node.right :
            return False
        return True

    def hasSum(self, root, hap, sum) :
        if self.isLeaf(root) :
            return hap == sum

        leftRet = False
        rightRet = False
        if root.left :
            leftRet = self.hasSum(root.left, hap+root.left.val, sum)
        if root.right :
            rightRet = self.hasSum(root.right, hap+root.right.val, sum)

        return (leftRet or rightRet)