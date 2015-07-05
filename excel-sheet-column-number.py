# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num=0
        lnth=len(s)
        for i in range(0,lnth) :
            c = s[lnth-(i+1)]
            index = ord(c) - 64
            num += index * pow(26,i)
        return num