# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = 0 
        temp = head 
        while temp:
            n+=1
            temp= temp.next
        temp = head   
        for i in range(n//2):
            temp = temp.next
            
        return temp   
    '''
        fast, slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    '''