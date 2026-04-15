# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head

        curr = head.next
        head.next = None
        
        while curr:
            fast = curr.next
            curr.next = head
            head = curr
            curr = fast

        return head