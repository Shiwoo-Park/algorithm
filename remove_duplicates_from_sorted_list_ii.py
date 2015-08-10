# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# coding:utf8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None

        retNode = head    # 반환해야하는 Head 노드
        rmexNode = head   # 끊어내기 시작직전 노드
        nowNode = head  # 현재노드
        nxtNode = head.next
        remove = False

        while nxtNode is not None :
            if nxtNode.val == nowNode.val :
                remove = True
            else :
                if remove :
                    nowNode.next = None

                    if nowNode.val == retNode.val : # 111 234 > 234
                        retNode = nxtNode

                    # 1 22 34 > 134
                    rmexNode.next = nxtNode
                    remove = False
                else :
                    rmexNode = nowNode
            nowNode = nxtNode
            nxtNode = nowNode.next

        if remove :
            rmexNode.next = None
            if nowNode.val == retNode.val : # 111 234 > 234
                retNode = None


        return retNode