# 203. Remove Linked List Elements

# 처음부터 확인 하다가 val과 같지 않은 val이면 더하고 removed 다음칸으로 이동
# 아니면 head만 한칸 뒤로 옮겨줌
# ***edge case***제일 마지막의 next 의 val이랑 같을 경우 따로 해결해죠라

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        removed = temp
        while head:
            if not head.val == val:
                removed.next = head
                removed = removed.next
            head = head.next
        if removed.next and removed.next.val == val:
            removed.next = None
        return temp.next