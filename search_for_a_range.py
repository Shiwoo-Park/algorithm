# https://leetcode.com/problems/search-for-a-range/

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l = len(A)
        ret = [-1,-1]
        started=False
        for i in range(0,l) :
            if A[i] == target :
                if not started :
                    started=True
                    ret[0] = i
            if started :
                if A[i] == target :
                    ret[1] = i
        return ret