class Point2D:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DoubleLinkNode:
    def __init__(self, _key, _val, _prev=None, _next=None):
        self.key = _key
        self.val = _val
        self.prev = _prev
        self.next = _next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
