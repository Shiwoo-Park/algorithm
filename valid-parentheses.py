# https://leetcode.com/problems/valid-parentheses/

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        l = len(s)
        pairDic = dict()
        pairDic["}"] = "{"
        pairDic[")"] = "("
        pairDic["]"] = "["
        for i in range(l) :
            c = s[i]
            if c in ["{","(","["] :
                stack.append(c)
            else :
                if stack : # more than one item in stack
                    top = stack.pop()
                    if top != pairDic[c] :
                        return False
                else :
                    return False
        if stack :
            return False
        else :
            return True