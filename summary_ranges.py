# https://leetcode.com/problems/summary-ranges/

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        sp = None
        ep = None
        ret = []
        for num in nums:
            if sp is not None:
                if ep+1 == num:
                    ep = num
                else:
                    if sp == ep:
                        ret.append("%s"%sp)
                    else:
                        ret.append("%s->%s"%(sp,ep))
                    sp = num
                    ep = num
            else:
                sp = num
                ep = num

        if sp is not None:
            if sp == ep:
                ret.append("%s"%sp)
            else:
                ret.append("%s->%s"%(sp,ep))

        return ret