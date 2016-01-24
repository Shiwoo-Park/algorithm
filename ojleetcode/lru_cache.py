# https://leetcode.com/problems/lru-cache/
# coding:utf-8

class Node:
	def __init__(self, _key, _val, _prev=None, _next=None):
		self.key = _key
		self.val = _val
		self.prev = _prev
		self.next = _next

class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		self.counter = 0
		self.capacity = capacity
		self.dic = dict()
		self.head = Node(None, None)  # OLD(least recent)
		self.tail = Node(None, None)  # MOST RECENT
		self.head.next = self.tail
		self.tail.prev = self.head

	# @return an integer
	def get(self, key):
		ret = -1
		if key in self.dic:
			t_node = self.dic[key]
			ret = t_node.val
			if t_node != self.tail.prev:
				# 현재 노드 제거
				t_prev_node = t_node.prev
				t_next_node = t_node.next
				t_prev_node.next = t_next_node
				t_next_node.prev = t_prev_node

				# 맨 뒤에 붙인다.
				most_recent_node = self.tail.prev
				most_recent_node.next = t_node
				t_node.prev = most_recent_node
				self.tail.prev = t_node
				t_node.next = self.tail
		return ret

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		if key in self.dic:
			target_node = self.dic[key]
			target_node.val = value
			t_prev_node = target_node.prev
			t_next_node = target_node.next
			t_prev_node.next = t_next_node
			t_next_node.prev = t_prev_node
		else:
			target_node = Node(key, value)
			# 자료구조에 넣는다.
			self.dic[key] = target_node
			self.counter += 1

		# 맨 뒤에 붙인다.
		most_recent_node = self.tail.prev
		most_recent_node.next = target_node
		target_node.prev = most_recent_node
		self.tail.prev = target_node
		target_node.next = self.tail

		if self.counter > self.capacity:
			most_old_node = self.head.next
			most_old_node.prev = None
			self.head.next = most_old_node.next
			self.head.next.prev = self.head
			most_old_node.next = None
			self.dic.pop(most_old_node.key)
			self.counter -= 1

