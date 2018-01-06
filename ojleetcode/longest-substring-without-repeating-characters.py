"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

The point is when I found the repeating character in currently collecting set.
I need to recollect from the cut index of current collected list (the point of repeated character)
, not starting a new collection with empty list

space complexity : O(N)
time complexity : O(N)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        keep_list = []
        keep_dic = {}

        for c in s:
            if c not in keep_dic:
                keep_list.append(c)
                keep_dic[c] = True
            elif c in keep_dic:
                collected_str = "".join(keep_list)
                if len(collected_str) > len(longest):
                    longest = collected_str
                cut_idx = keep_list.index(c)
                for i in range(cut_idx):
                    del keep_dic[keep_list[i]]
                keep_list = keep_list[cut_idx + 1:]
                keep_list.append(c)

                # print("LIST:%s"%keep_list)
                # print("DIC:%s"%keep_dic)

        if len(longest) < len(keep_list):
            longest = "".join(keep_list)

        # print("RETURN:",len(longest))
        return len(longest)