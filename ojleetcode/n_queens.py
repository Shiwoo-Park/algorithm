# https://leetcode.com/problems/n-queens/

class Solution:
	# @param {integer} n
	# @return {string[][]}
	def solveNQueens(self, n):
		if n == 1:
			return [["Q"]]
		if n < 4:
			return []

		ret_list = []
		self.putNextQueen(ret_list, [], {}, n)
		return ret_list

	def putNextQueen(self, ret_list, now_ret, queen_pos_dic, n):
		rows = len(now_ret)
		if rows == n:
			ret_list.append(now_ret)
			return

		for i in range(n):
			check_point = (rows, i)
			if self.isAvailable(check_point, queen_pos_dic):
				row = []
				for k in range(n):
					if k == i:
						row.append("Q")
					else:
						row.append(".")
				new_ret = list(now_ret)
				new_ret.append("".join(row))
				new_pos_dic = dict(queen_pos_dic)
				new_pos_dic[rows] = i
				self.putNextQueen(ret_list, new_ret, new_pos_dic, n)

	def isAvailable(self, chk_point, queen_pos_dic):
		ret = True
		for row, col in queen_pos_dic.items():
			if self.canKill(chk_point, (row, col)):
				ret = False
				break
		return ret

	def canKill(self, point1, point2):
		if point1[0] == point2[0]:
			return True
		if point1[1] == point2[1]:
			return True
		if abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
			return True
		return False