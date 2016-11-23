# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# unsolved yet...


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        # return "Node(%s, L[%s], R[%s])" % (self.val, self.left, self.right)
        return "Node(%s)" % (self.val)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = []
        self.visit(root, p, q, stack, {})
        return stack.pop()

    def visit(self, r, n1, n2, stack, found):
        if not r:
            return
        if len(found) == 2:
            return

        print("\nvisit:", r, " \nstack:", len(stack), "\nfound:",found)

        # value check
        if len(found) == 0:  # 미발견
            if r.val == n1.val:
                found[1] = r.val
            elif r.val == n2.val:
                found[1] = r.val
        else:  # 1개 발견
            if r.val == n1.val:
                found[2] = r.val
            elif r.val == n2.val:
                found[2] = r.val

        org_found = len(found)
        if org_found < 2:
            print("+++ stack append:", r)
            stack.append(r)
        self.visit(r.left, n1, n2, stack, found)
        if len(found) == 2:
            return
        self.visit(r.right, n1, n2, stack, found)
        # if len(found) == org_found:
        if len(found) < 2:
            poped = stack.pop()
            print("--- stack pop:", poped)


class Solution2:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        info = {'root': root, 'n1': p, 'n2': q, 'f1': False, 'f2': False, 'fc':0, 'ret': root}
        self.visit(root, info)
        return info['ret']

    def visit(self, r, info):
        print("Visit:",r, " / found_count: ", info['fc'])
        if not r:
            return
        if info['fc'] == 2:
            return

        tmp = info['fc']
        if r == info['n1']:
            info['f1'] = True
            info['fc'] += 1
        elif r == info['n2']:
            info['f2'] = True
            info['fc'] += 1
        if tmp == 1 and info['fc'] == 2:
            return

        tmp = info['fc']
        self.visit(r.left, info)
        if tmp == 1 and info['fc'] == 2:
            info['ret'] = r

        tmp = info['fc']
        self.visit(r.right, info)
        if tmp == 1 and info['fc'] == 2:
            info['ret'] = r

