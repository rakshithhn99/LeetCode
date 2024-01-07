# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or head.next is None :
            return False 
        
        if head.next == head:
            return True 
        
        slow = head; fast = slow.next
        while fast and slow != fast:
            slow = slow.next 
            if fast.next is None:
                return False
            fast = fast.next.next
        
        if fast is None:
            return False
        
        return True

        