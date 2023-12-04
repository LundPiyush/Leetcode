# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2= l1,l2
        dummy = ListNode()
        cur = dummy
        carry,sum = 0,0
        
        while temp1!=None or temp2!=None:
            sum = carry
            if temp1:
                sum = sum + temp1.val
            if temp2:
                sum = sum + temp2.val
                
            newNode = ListNode(sum%10)
            carry = sum //10
            
            cur.next = newNode
            cur = newNode
            
            if temp1: 
                temp1= temp1.next
            if temp2: 
                temp2= temp2.next
                
        if carry:
            newNode = ListNode(carry)
            cur.next = newNode
        return dummy.next
            