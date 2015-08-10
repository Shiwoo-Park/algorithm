# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        lead = head
        follow = head
        counter = 0
        while lead.next :
            lead = lead.next
            if counter == n :
                follow = follow.next
            else :
                counter += 1
        if counter == n :
            try :
                rmNode = follow.next
                follow.next = rmNode.next
                rmNode.next = None
            except :
                return None
        else :
            return head.next
        return head

