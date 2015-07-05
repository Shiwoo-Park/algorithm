# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        total = 0
        divide = 5
        while n >= divide:
            total += n / divide
            divide = divide * 5
        return total