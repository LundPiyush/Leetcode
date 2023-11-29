# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        p = head
        count = 0
        while p:
            p= p.next 
            count +=1
        
        nth_node = count - n # 5 - 2 = 3
        
        cur = head
        prev = None
        for i in range(nth_node):
            prev = cur
            cur = cur.next
    # if prev is None it means nth_node is 0 which means list length is x(say 3) nodes and they
    # have asked to delete 3rd node from last which means 1st node of the list. Hence, we return head.next
        if prev == None:
            return head.next
        prev.next = cur.next
        cur.next = None
        
        return head
            
            