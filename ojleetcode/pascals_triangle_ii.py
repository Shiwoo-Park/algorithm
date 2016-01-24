# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:

    # @return a list of integers
    # Given an index k, return the kth row of the Pascal's triangle.
    # Use only O(n) extra spaces

    def getRow(self, rowIndex):
        if rowIndex == 0 :
            return [1]
        if rowIndex == 1 :
            return [1,1]
        base = [1,1]
        for i in range(0,rowIndex-1) :
            for j in range(0, len(base)-1) :
                base[j] = base[j] + base[j+1]
            base.insert(0, 1)

        return base