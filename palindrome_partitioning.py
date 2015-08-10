# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        palin_dic = dict()
        for i in range(len(s)):
            palin_dic[i] = self.getPalindroms(s[i:])
        ret = []
        self.collect(ret, palin_dic, len(s), 0, [])
        return ret

    def getPalindroms(self, s):
        ret = []
        s_len = len(s)
        for i in range(s_len):
            word = s[:s_len-i]
            if self.isPalindrome(word):
                ret.append(word)
        return ret

    def isPalindrome(self, s):
        sid = 0
        eid = len(s)-1
        ret = True
        while True:
            if sid > eid:
                break
            front = s[sid]
            back = s[eid]
            if front != back:
                ret = False
                break
            sid += 1
            eid -= 1
        return ret

    def collect(self, ret, palin_dic, idx_limit, start_idx, current_collection):
        append_list = palin_dic[start_idx]
        for palin_str in append_list:
            new_start_idx = start_idx + len(palin_str)
            new_collection = list(current_collection)
            new_collection.append(palin_str)
            if new_start_idx >= idx_limit:
                ret.append(new_collection)
            else:
                self.collect(ret, palin_dic, idx_limit, new_start_idx, new_collection)