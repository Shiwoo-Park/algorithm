# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
	# @param root, a binary search tree's root node
	def __init__(self, root):
		self.preorder_str = ""
		self.num_idx = 1
		if root:
			self.preorderSearch(root)
		self.preorder_str_len = len(self.preorder_str)

	def preorderSearch(self, node):
		if node.left:
			self.preorderSearch(node.left)
		self.preorder_str += ";%s"%node.val
		if node.right:
			self.preorderSearch(node.right)

	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		ret = True
		if self.num_idx >= self.preorder_str_len:
			ret = False
		return ret

	# @return an integer, the next smallest number
	def next(self):
		num = self.preorder_str[self.num_idx]
		self.num_idx += 1
		while (self.num_idx < self.preorder_str_len):
			c = self.preorder_str[self.num_idx]
			if c == ";":
				self.num_idx += 1
				break
			num += self.preorder_str[self.num_idx]
			self.num_idx += 1
		return int(num)


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())