# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):   
        lst = []
        while head:
            lst.append(head)
            head = head.next
        return lst[len(lst) // 2]