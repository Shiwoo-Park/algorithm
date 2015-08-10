import os
from n_queens import Solution

if __name__ == "__main__":
	s = Solution()
	rets = s.solveNQueens(5)
	for ret in rets:
		for row in ret:
			print row
		print "====================="

	# files = os.listdir(".")
	# for file in files:
	# 	os.rename(file, file.replace("-", "_"))