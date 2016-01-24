# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(16) :
            msb = (n >> (31-i)) & 1 # from right side bit
            lsb = (n >> i) & 1 # from left side bit
            result |= msb << i
            result |= lsb << (31-i)
        return result

class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        l = 32-len(s)
        for i in range(l) :
            s = "0"+s
        return int(s[::-1],2)

