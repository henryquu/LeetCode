# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        prev = False
        while head:
            if prev == True:
                prev = False
                middle = middle.next
            else:
                prev = True
            head = head.next
        return middle