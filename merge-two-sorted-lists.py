# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = None
        now_node = None

        while (l1 is not None) or (l2 is not None):
            next_node = None
            if (l1 is not None) and (l2 is not None):
                if l1.val < l2.val:
                    next_node = l1
                    l1 = l1.next
                else:
                    next_node = l2
                    l2 = l2.next
            elif l1 is not None:
                next_node = l1
                l1 = l1.next
            elif l2 is not None:
                next_node = l2
                l2 = l2.next
            if next_node is not None:
                if head is None:
                    head = next_node
                if now_node is None:
                    now_node = next_node
                else:
                    now_node.next = next_node
                    now_node = now_node.next

        return head