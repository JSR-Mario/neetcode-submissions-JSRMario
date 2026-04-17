# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        queue = deque()

        reader = head
        for i in range(left-1):
            reader = reader.next
        
        writter = reader
        queue.append(reader.val)
        for i in range(right-left):
            reader = reader.next
            queue.append(reader.val)
        
        while queue:
            writter.val = queue.pop()    
            writter = writter.next
        
        return head