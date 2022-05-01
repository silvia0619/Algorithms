# 876. Middle of the Linked List
# 완전 빨리 풀음
# 하나는 매번 가고 하나는 하나 건너서 가고 
# 하나 건너서 간거 return

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        half = head
        halfCheck = False
        while temp:
            temp = temp.next
            if halfCheck:
                half = half.next
                halfCheck = False
            else:
                halfCheck = True
        return half