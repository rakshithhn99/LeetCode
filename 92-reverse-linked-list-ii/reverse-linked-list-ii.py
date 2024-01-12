# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        
        prev_left = None; left_ptr = None; curr=head; prev = None
        count = 0
        while count < right:
            count+=1
            if count == left-1:
                prev_left = curr 
            
            if count < left:
                curr = curr.next
                continue
            
            if count == left:
                left_ptr = curr 
            
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        
        print(curr)
        print(prev)
        print(prev_left)
        print(left_ptr)

        if prev_left:
            prev_left.next = prev
            left_ptr.next = curr 
            return head 
        
        left_ptr.next = curr 
        return prev


        