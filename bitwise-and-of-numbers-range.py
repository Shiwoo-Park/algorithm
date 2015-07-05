# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        bm = bin(m)[2:]
        bn = bin(n)[2:]
        lm = len(bm)
        ln = len(bn)

        if lm != ln:
            return 0

        ret = ""
        bit_changed = False
        for i in range(0, lm):
            m_bit = bm[i]
            n_bit = bn[i]
            if bit_changed:
                ret += "0"
            else:
                if m_bit != n_bit:
                    bit_changed = True
                    ret += "0"
                else:
                    ret += m_bit
        return int(ret,2)