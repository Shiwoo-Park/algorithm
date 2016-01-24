# https://leetcode.com/problems/palindrome-number/

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False

        s = str(x)
        limit = len(s) / 2
        for i in range(0, limit):
            if s[i] != s[-(i+1)]:
                return False
        return True