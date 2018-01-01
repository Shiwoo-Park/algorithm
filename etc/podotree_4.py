# coding=utf-8
import sys


# s =
# sArr = s.split("*")
# print sArr
# s2Arr = []
# isAppeared = False
# for elem in sArr:
#     if elem != '':
#         s2Arr.append(elem)
# result = "*".join(s2Arr)
# if sArr[0] == '':
#     result = "*" + result
# if sArr[-1] == '' and len(sArr) > 2:
#     result = result + "*"
# print result

# simply match words
def matchWord(textWord, expWord):
    print "matchWord:", textWord, "/", expWord
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


# print matchWord("abc", "a?c")
# print matchWord("abc", "a??")
# print matchWord("abc", "a?b")
# print matchWord("abc", "a")
# print matchWord("abc", "???")
# print matchWord("abc", "?")
# print matchWord("c", "?")

# find possible start points
def getPoints(s, c, startPoint, endPoint):
    # length optimization
    print "getPoints of [%s] in [%s] index of %s ~ %s" % (c, s, startPoint, endPoint)
    ret = []
    for i in range(startPoint, endPoint):
        if s[i] == c:
            ret.append(i)
    return ret


def matchWildCard(txt, expArr, idxTxtFront, idxTxtEnd, idxExpArrFront, idxExpArrEnd):
    print "txtFront:%s / txtEnd:%s / expArrFront(%s): %s / expArrEnd(%s): %s" \
          % (idxTxtFront, idxTxtEnd, idxExpArrFront, expArr[idxExpArrFront], idxExpArrEnd, expArr[idxExpArrEnd])
    if idxExpArrFront > idxExpArrEnd:
        return True
    if idxTxtFront >= idxTxtEnd:
        return True
    nowExp = expArr[idxExpArrFront]
    nowExpLen = len(nowExp)
    points = getPoints(txt, nowExp[0], idxTxtFront, idxTxtEnd)
    print points
    if len(points) == 0:
        return False
    for point in points:
        if point + nowExpLen > idxTxtEnd:
            continue
        # 하나만이라도 찾으면 True
        if matchWord(txt[point:point + nowExpLen], nowExp):
            if matchWildCard(txt, expArr, point + nowExpLen, idxTxtEnd, idxExpArrFront + 1, idxExpArrEnd):
                return True
    return False

def getMatchResult(text, exp):
    print "============================"

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

    print "Text : ", text
    print "Final Exp : ", finalExp
    print "Exp Array : ", expArr

    if len(expArr) == 1:
        return matchWord(text, exp)
    try:
        textLen = len(text)
        expArrLen = len(expArr)
        # character index of text
        idxTxtFront = 0
        idxTxtEnd = textLen - 1
        # id of expression array
        idxExpArrFront = 0
        idxExpArrEnd = expArrLen - 1

        print "Initial state : txtFront:%s / txtEnd:%s / expArrFront:%s / expArrEnd:%s\n" \
              % (idxTxtFront, idxTxtEnd, idxExpArrFront, idxExpArrEnd)

        if expArr[0] != '':  # front matching
            if not matchWord(text[:len(expArr[0])], expArr[0]):
                return False
            idxTxtFront += len(expArr[0])
        idxExpArrFront += 1

        if expArr[-1] != '':  # end matching
            if not matchWord(text[-len(expArr[-1]):], expArr[-1]):
                return False
            idxTxtEnd -= len(expArr[-1])
        idxExpArrEnd -= 1

        if len(expArr) == 2:
            return True

        # status : *abc*
        return matchWildCard(text, expArr, idxTxtFront, idxTxtEnd, idxExpArrFront, idxExpArrEnd)

    except Exception as e:  # parsing error
        return False

        # while idxExpArrFront < idxExpArrEnd:
        #     nowExp = expArr[idxExpArrFront]
        #     print "nowExp : ", nowExp
        #     if nowExp == '':  # wildcard:
        #         if idxExpArrFront == 0:
        #             idxExpArrFront += 1
        #             continue
        #         return True
        #
        #     points = getPoints(text, nowExp[0], idxTxtFront, idxTxtEnd)
        #     if len(points) == 0:
        #         return False
        #     for point in points:
        #         if matchWord(text[point:len(nowExp)], nowExp):
        #     exit(0)


print getMatchResult("", "?")
print getMatchResult("", "*")
print getMatchResult("", "**")
print getMatchResult("", "***")
print getMatchResult("abcdeft", "abc??ft")
print getMatchResult("abcdeft", "abd*")
print getMatchResult("abcdeftabc", "*abc")
print getMatchResult("welifjabaweiabcedffjabcdadigjbabcdefabcawelijf", "*f?a**abc***abcawel*")
# print getMatchResult("abcdefabcabcdabelkrienabclsiefnasbcabcdfff", "abc****ab**b***c*d**fff")

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
#     print getMatchResult(text, exp)
#
#     print text, "/", exp
#     line = sys.stdin.readline().strip()
#     caseCount += 1
