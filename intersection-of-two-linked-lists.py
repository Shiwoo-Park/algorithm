# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None :
            return None

        stackA = [headA.val]
        stackB = [headB.val]

        nextNode = headA.next
        while nextNode is not None :
            stackA.append(nextNode.val)
            nextNode = nextNode.next

        nextNode = headB.next
        while nextNode is not None :
            stackB.append(nextNode.val)
            nextNode = nextNode.next

        noIntersection = True
        lastA = stackA[-1]
        lastB = stackB[-1]
        while lastA == lastB :
            noIntersection = False
            stackA.pop()
            stackB.pop()
            try :
                lastA = stackA[-1]
                lastB = stackB[-1]
            except :
                break

        if noIntersection :
            return None

        counter = 0
        nextNode = headA
        while counter != len(stackA) :
            counter += 1
            if nextNode.next :
                nextNode = nextNode.next
            else :
                break

        return nextNode

