# https://leetcode.com/problems/min-stack/

class MinStack:
	def __init__(self):
		self.topkey = -1
		self.minVal = None
		self.stack = []

	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.topkey += 1
		self.stack.append(x)
		if self.minVal is None:
			self.minVal = x
		else:
			if x < self.minVal:
				self.minVal = x

	# @return nothing
	def pop(self):
		topVal = self.stack[self.topkey]
		refreshMin = False
		if topVal == self.minVal:
			refreshMin = True
		self.stack.pop()
		self.topkey -= 1
		if refreshMin:
			if self.topkey > -1:
				self.minVal = min(self.stack)
			elif self.topkey == -1:
				self.minVal = None


	# @return an integer
	def top(self):
		if self.topkey != -1:
			return self.stack[self.topkey]
		else:
			return None


	# @return an integer
	def getMin(self):
		return self.minVal


class MinStack2:

	def __init__(self) :
		self.stack = []
		self.sTop = -1
		self.minStack = []
		self.minTop = -1

	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.stack.append(x)
		self.sTop += 1

		if self.minStack :
			minVal = self.minStack[self.minTop]
			if minVal >= x :
				self.minStack.append(x)
				self.minTop += 1
		else :
			self.minStack.append(x)
			self.minTop += 1

	# @return nothing
	def pop(self):
		if self.stack :
			popVal = self.stack[self.sTop]
			self.stack.pop()
			self.sTop -= 1

			if self.minStack :
				min = self.minStack[self.minTop]
				if min == popVal :
					self.minStack.pop()
					self.minTop -= 1

	# @return an integer
	def top(self):
		if self.stack :
			return self.stack[self.sTop]

	# @return an integer
	def getMin(self):
		if self.minStack :
			return self.minStack[self.minTop]