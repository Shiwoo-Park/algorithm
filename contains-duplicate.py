# https://leetcode.com/problems/contains-duplicate/

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = dict()
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False