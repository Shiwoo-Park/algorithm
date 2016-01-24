# https://leetcode.com/problems/triangle/

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        depth = len(triangle)
        if depth < 2 :
            return triangle[0][0]
        for d in range(depth-1, 0,-1):
            for i in range(0, d):
                if triangle[d][i] > triangle[d][i+1] :
                    triangle[d-1][i] = triangle[d-1][i] + triangle[d][i+1]
                else:
                    triangle[d-1][i] = triangle[d-1][i] + triangle[d][i]

        return triangle[0][0]