# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        stack.append((")",-1))
        l = len(s)
        max = 0
        for i in range(0, l):
            if s[i] == "(" :
                stack.append(("(",i))
            else :   # ")"
                top = stack[-1]
                if top[0] == "(" :
                    stack.pop()
                    top = stack[-1]
                    cmax = i - top[1]
                    if cmax > max :
                        max = cmax
                else :
                    stack.append((")",i))
        return max