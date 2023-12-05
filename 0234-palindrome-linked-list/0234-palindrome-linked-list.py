# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        cur= head
        prev,next_p= None,None
        
        while cur:
            next_p = cur.next
            cur.next = prev
            prev = cur
            cur = next_p
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast= head,head
        
        while fast.next != None and fast.next.next !=None:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = self.reverseList(slow.next)
        
        dummy = head
        
        slow = slow.next
        
        while slow!=None:
            if slow.val != dummy.val:
                return False
            slow = slow.next
            dummy = dummy.next
        return True
        
            