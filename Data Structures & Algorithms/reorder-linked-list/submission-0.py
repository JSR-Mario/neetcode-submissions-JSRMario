# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i=0
        counter = head
        while counter:
            i+=1
            counter = counter.next
        cut = math.ceil(i/2)

        start = head
        for _ in range(cut):
            start = start.next
        
        # now we reverse start
        prev = None
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        

        util = ListNode(0,head)

        while head and prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp

            head = temp
            prev = temp2
        
        if head:
            head.next = prev
        else:
            prev.next = head