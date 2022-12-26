# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        while l1 or l2:
            if l2:
                l1.val += l2.val
                l2 = l2.next

            if l1.val > 9:
                l1.val -= 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            
            if l2 and not l1.next:    
                l1.next = ListNode()

            l1 = l1.next

        return head
            
