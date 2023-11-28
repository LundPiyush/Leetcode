# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # Brute force approach 
        
        n = 0 
        temp = head 
        # counting nodes in LinkedList
        while temp:
            n+=1
            temp= temp.next
            
        temp = head   
        # traversing n/2 times to find the middle node
        for i in range(n//2):
            temp = temp.next
            
        return temp   
    '''
        # Hare-Tortoise approach
        
        fast, slow = head,head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    