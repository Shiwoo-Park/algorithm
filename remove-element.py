# https://leetcode.com/problems/remove-element/

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        list = []
        arr_len = len(A)
        for i in range(arr_len) :
            if A[i] == elem :
                list.append(i)

        list_len = len(list)
        for j in range(list_len-1,-1,-1) :
            del A[list[j]]

        return len(A)