# 141. Linked List Cycle

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