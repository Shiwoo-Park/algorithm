# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def getPrefix(self, a, b) :
        l = len(a)
        if len(b) < l :
            l = len(b)
        prefix = ""
        for i in range(0,l) :
            if a[i] == b[i] :
                prefix += a[i]
            else :
                break
        return prefix

    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 :
            return ""
        if len(strs) == 1 :
            return strs[0]
        longestPrefix = self.getPrefix(strs[0], strs[1])
        if len(strs) == 2 :
            return longestPrefix
        for i in range(2, len(strs)) :
            s = strs[i]
            if s.startswith(longestPrefix) :
                continue
            else :
                longestPrefix = self.getPrefix(longestPrefix, s)
            if longestPrefix == "" :
                break
        return longestPrefix
