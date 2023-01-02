# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = None
        fast = head

        k = 0
        while fast.next:
            k += 1
            fast = fast.next
            if k >= n:
                if slow:
                    slow = slow.next
                else:
                    slow = head

        if not slow: 
            return head.next
        elif slow.next:
            slow.next = slow.next.next
        return head