# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head #start slow from start
                while fast!=slow: # covering L1 distance to find the starting point
                    fast= fast.next
                    slow = slow.next
                return slow
        return None
            
        