# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        count = 0
        while p:
            p= p.next 
            count +=1
        
        nth_node = count - n # 5 - 2 = 3
        
        cur = head
        prev = None
        while nth_node > 0:
            prev = cur
            cur = cur.next
            nth_node -=1
        if prev == None:
            return head.next
        prev.next = cur.next
        cur.next = None
        
        return head
            
            