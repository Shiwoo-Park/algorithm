# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    # @return an integer
    def atoi(self, str):
        s = str.strip()
        isMinus = False
        snum = ""
        for i in range(0, len(s)) :
            c = s[i]
            if self.isInt(c) :
                snum += c
            else :
                if i==0 and c in ["+","-"] :
                    if c == "-" :
                        isMinus = True
                    continue
                break

        if snum == "" :
            return 0
        else :
            n = int(snum)
            if n >= 2147483647 :
                if isMinus :
                    if n == 2147483647 :
                        return -2147483647
                    else :
                        return -2147483648
                else :
                    return 2147483647
            else :
                if isMinus :
                    return -n
                else :
                    return n


    def isInt(self, n):
        try:
            int(n)
            return True
        except :
            return False