# https://leetcode.com/problems/majority-element/

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate = None
        count = 0
        for n in num:
            if candidate == None:
                candidate = n
                count += 1
            elif n == candidate:
                count += 1
            elif n != candidate and count == 1:
                candidate = None
                count -= 1
            elif n != candidate:
                count -= 1
        return candidate