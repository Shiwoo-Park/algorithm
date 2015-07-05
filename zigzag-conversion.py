# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1 :
            return s

        wordArr = []
        for i in range(0,nRows) :
            wordArr.append("")

        dirDown = True
        for i in range(0, len(s)) :
            letter = s[i]
            quotient = i/(nRows-1)
            remainder = i%(nRows-1)

            if dirDown :
                if remainder == 0 :
                    if quotient%2 == 0 :
                        wordArr[0] += letter
                    else :
                        wordArr[nRows-1] += letter
                        dirDown = False
                else :
                    wordArr[remainder] = wordArr[remainder]+s[i]
            else :
                if remainder == 0 :
                    if quotient%2 == 0 :
                        wordArr[0] += letter
                        dirDown = True
                    else :
                        wordArr[nRows-1] += letter

                else :
                    wordArr[(nRows-1) - remainder] = wordArr[(nRows-1) - remainder]+s[i]

        ret = ""
        for i in range(0,len(wordArr)) :
            ret += wordArr[i]

        return ret