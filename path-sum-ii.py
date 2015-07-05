# https://leetcode.com/problems/path-sum-ii/

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        paths = []
        path = []
        if root :
            self.getPath(root, sum, 0, path, paths)
        return paths

    def getPath(self, root, sum, mysum, path, paths):
        if (not root.left) and (not root.right) : # is Leaf
            if mysum + root.val == sum :
                newPath = list(path)
                newPath.append(root.val)
                paths.append(newPath)
        else : # not Leaf
            path.append(root.val)
            mysum += root.val
            if root.left :
                self.getPath(root.left, sum, mysum, path, paths)
            if root.right :
                self.getPath(root.right, sum, mysum, path, paths)
            path.pop()