# https://leetcode.com/problems/length-of-last-word/

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        fl = len(s)
        idx = s.rfind(" ")

        return fl - (idx+1)
