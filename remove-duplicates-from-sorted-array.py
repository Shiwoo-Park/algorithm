# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        l = len(nums)
        counter = 0
        now_val = None
        for i in range(l):
            num = nums[counter]
            count = True
            if now_val is None:
                now_val = num
            else:
                if num == now_val: # dup
                    del nums[counter]
                    count = False
                else:
                    now_val = num
            if count:
                counter += 1

        return counter