# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ret = 0
        v1List = version1.split(".")
        v2List = version2.split(".")

        l = len(v1List)
        if len(v2List) > l :
            l = len(v2List)

        for i in range(0, l) :
            num1 = 0
            num2 = 0
            if i <len(v1List) :
                num1 = int(v1List[i])
            if i <len(v2List) :
                num2 = int(v2List[i])

            if num1 > num2 :
                ret = 1
                break
            if num1 < num2 :
                ret = -1
                break

        return ret
