# https://leetcode.com/problems/rotate-array/

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)
        if k == 0 :
            return
        newArr = []
        k = k%l
        for i in range(0, l) :
            newArr.append(nums[i-k])
        for i in range(0,l) :
            nums[i] = newArr[i]