# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        front = 0
        back = 0
        sum = nums[0]
        arr_len = len(nums)
        min_len = len(nums)
        solved = False

        while back < arr_len:
            if sum >= s:
                solved = True
                current_len = back - front + 1
                if current_len < min_len:
                    min_len = current_len
                sum = sum - nums[front]
                front += 1
            else:
                back += 1
                if back < arr_len:
                    sum = sum + nums[back]

        if solved:
            return min_len
        else:
            return 0