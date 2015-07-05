# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        retList = []
        if root :
            self.visitNode(root, retList, 0)
        return retList

    def visitNode(self, node, retList, depth) :
        if len(retList) <= depth :
            retList.insert(0,[])
        depthList = retList[-(depth+1)]
        depthList.append(node.val)
        if node.left :
            self.visitNode(node.left, retList, depth+1)
        if node.right :
            self.visitNode(node.right, retList, depth+1)