# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return head
        now_node = head
        next_node = head.next
        head.next = None
        while next_node:
            back_node = now_node
            now_node = next_node
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = None
            now_node.next = back_node
        return now_node