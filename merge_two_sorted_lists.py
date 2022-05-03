# 21. Merge Two Sorted Lists

# 둘중에 하나가 끝날때 까지 두개 비교해서 작은거 넣기
# 다 끝났으면 list1 or list2 중에 남은거 넣어주기

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0)      # 제일 처음 Node는 dummy 그냥 root를 지정해주기 위해 있음
        merged = temp
        while list1 and list2:
            if list1.val > list2.val:
                merged.next = list2
                list2 = list2.next
            else:
                merged.next = list1
                list1 = list1.next
            merged = merged.next
        merged.next = list1 or list2
        return temp.next        # return 할때는 dummy빼고 return