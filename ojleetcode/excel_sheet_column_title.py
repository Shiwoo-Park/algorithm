# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    # @return a string
    def convertToTitle(self, num):
        self.sList = ["Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
        return self.rec(num,"")

    def rec(self, num, s):
        q = num/26
        r = num%26

        if r == 0 :
            q = q - 1

        if q < 1 :
            s = self.sList[r] + s
            return s
        else :
            s = self.sList[r] + s
            return self.rec(q,s)