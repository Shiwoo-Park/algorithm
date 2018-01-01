# Please use Python 2
# coding=utf-8
import sys

class Solution(object):
    # simply match words
    def matchWord(self, textWord, expWord):
        l1 = len(textWord)
        l2 = len(expWord)
        if l1 != l2:
            return False
        if l1 == 0:
            return True
        p1 = 0
        for i in range(l2):
            c = expWord[i]
            if c != "?":
                if c != textWord[p1]:
                    return False
            p1 += 1
        return True

    # find possible start points
    def getPoints(self, s, c, startPoint, endPoint):
        ret = []
        for i in range(startPoint, endPoint):
            if s[i] == c:
                ret.append(i)
        return ret

    # recursive whildcard matching
    def matchWildCard(self, txt, expArr, idxTxtFront, idxTxtEnd, idxExpArrFront, idxExpArrEnd):
        print "txtFront:%s / txtEnd:%s / expArrFront(%s): %s / expArrEnd(%s): %s" \
          % (idxTxtFront, idxTxtEnd, idxExpArrFront, expArr[idxExpArrFront], idxExpArrEnd, expArr[idxExpArrEnd])
        if idxExpArrFront > idxExpArrEnd:
            return True
        if idxTxtFront >= idxTxtEnd:
            return True
        nowExp = expArr[idxExpArrFront]
        nowExpLen = len(nowExp)
        points = self.getPoints(txt, nowExp[0], idxTxtFront, idxTxtEnd)
        if len(points) == 0:
            return False
        for point in points:
            if point + nowExpLen > idxTxtEnd:
                continue
            if self.matchWord(txt[point:point + nowExpLen], nowExp):
                if self.matchWildCard(txt, expArr, point + nowExpLen, idxTxtEnd, idxExpArrFront + 1, idxExpArrEnd):
                    return True
        return False

    # main function
    def isMatch(self, text, exp):

        # trim duplicated wildcard
        tmpArr1 = exp.split("*")
        tmpArr2 = []
        idx = 0
        for elem in tmpArr1:
            if idx == 0 or idx == len(tmpArr1) - 1:
                tmpArr2.append(elem)
            elif elem != '':
                tmpArr2.append(elem)
            idx += 1
        finalExp = "*".join(tmpArr2)

        # start matching
        if finalExp == "*":
            return True
        expArr = finalExp.split("*")

        if len(expArr) == 1:
            return self.matchWord(text, exp)
        try:
            textLen = len(text)
            expArrLen = len(expArr)

            # character index of text
            idxTxtFront = 0
            idxTxtEnd = textLen - 1

            # id of expression array
            idxExpArrFront = 0
            idxExpArrEnd = expArrLen - 1

            if expArr[0] != '':  # front matching
                if not self.matchWord(text[:len(expArr[0])], expArr[0]):
                    return False
                idxTxtFront += len(expArr[0])
            idxExpArrFront += 1

            if expArr[-1] != '':  # end matching
                if not self.matchWord(text[-len(expArr[-1]):], expArr[-1]):
                    return False
                idxTxtEnd -= len(expArr[-1])
            idxExpArrEnd -= 1

            if len(expArr) == 2:
                return True

            # status : both ends are wildcard (ex. *xxxxxxxx*)
            return self.matchWildCard(text, expArr, idxTxtFront, idxTxtEnd, idxExpArrFront, idxExpArrEnd)

        except Exception as e:  # parsing error
            return False

s = Solution()
a = "aaabaabbbbaaaaabaabbababbaaabbabaabaaabaaaaaabbabaabaaababbbabbaaaaaaaaaabaaaabbabaabbbbaabaaabaabaabbbbabaabbbaababaaaaabbabaabbbababaaaaaabbabaaababbbaabaaababbbbabbbabbbabbabbbaabbbbabaaaababaaabbaaa"
b = "a**bbb****baab****b**bab**abb*abb***aab*********bab*bba*abbbab*baaababaa*a****b*****a**aaabab*bb*b*a*"
a = "aaabaabbbbaaaaabaabbababbaaabbabaabaaabaaaa"
b = "a**bbb****baab****b*"
print s.isMatch(a, b)

#
# line = sys.stdin.readline().strip()
#
# totalCaseCount = int(line)
# if totalCaseCount == 0:
#     exit(0)
#
# line = sys.stdin.readline().strip()
# caseCount = 1

# while line:
#     if caseCount > totalCaseCount:
#         print("Invalid Input")
#         exit(1)
#     caseArr = line.split()
#     text = caseArr[0]
#     exp = caseArr[1]
#
#     print s.isMatch(text, exp)
#
#     line = sys.stdin.readline().strip()
#     caseCount += 1
#
#
