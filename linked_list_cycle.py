# 141. Linked List Cycle
# 답지 봤는데 이게 왜 되는지 모르겠음

# 3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> ...
# slow: 3 / 2 / 0 / 4 / 2 / 0 / 4 / 2 / 0 / 4 ...
# fast: 2 / 4 / 0 / 2 / 4 / 0 / ...

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next:
            slow = head
            fast = head.next
            while fast.next and fast.next.next:
                if slow is fast:
                    return True
                fast = fast.next.next
                slow = slow.next
        return False