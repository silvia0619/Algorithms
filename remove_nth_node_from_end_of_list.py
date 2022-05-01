# 19. Remove Nth Node From End of List

# last는 끝을 찾을 때 까지 하나씩 가고
# temp는 n+1 만큼의 간격을 두고 last앞에서 한칸씩 가
# last를 찾았을때 temp는 remove 해야할 node의 전 node
# 제일 첫 node 면 head 옮겨주고 중간이면 temp.next = temp.next.next 
# temp.next 가 없다는건 remove할 노드 밖에 없다는거

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        last = head
        counter = n + 1
        while last:
            last = last.next
            if counter == 0:
                temp = temp.next
            else:
                counter -= 1
        if counter > 0:
            head = head.next
            return head
        elif temp.next:
            temp.next = temp.next.next
        else:
            head = None
        return head