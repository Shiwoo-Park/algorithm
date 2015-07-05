# https://leetcode.com/problems/count-and-say/

class Solution:
    # @param {integer} n
    # @return {string}
    def getNext(self, s):
        now_c = s[0]
        c_cnt = 1
        ret = ""
        s_len = len(s)
        for i in range(1, s_len):
            c = s[i]
            if c == now_c:
                c_cnt += 1
            else:
                ret += "%s%s"%(c_cnt, now_c)
                c_cnt = 1
                now_c = c
        ret += "%s%s"%(c_cnt, now_c)
        return ret

    def countAndSay(self, n):
        word = "1"
        for i in range(n-1):
            word = self.getNext(word)
        return word