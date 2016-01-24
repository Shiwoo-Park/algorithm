# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        l = len(nums)
        sp = 0

        for i in range(l):
            n = nums[i]

            if (i-sp) > k:
                d.pop(nums[sp])
                sp += 1

            if n in d:
                return True
            else:
                d[n] = 1

        return False