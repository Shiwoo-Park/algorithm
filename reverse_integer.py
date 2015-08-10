# https://leetcode.com/problems/reverse-integer/

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        isMinus = False
        s = str(x)
        if x < 0:
            isMinus = True
            s = s[1:]
        s = s[::-1]
        ret = int(s)
        if (ret > 2147483647) or (ret < -2147483648):
            return 0
        if isMinus:
            ret = ret * -1
        return ret