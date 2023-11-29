# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #using one traversal
        #TC -> O(N)
        #SC -> O(1)
        
        fast = head
        for i in range(n): # move fast by n steps 
            fast = fast.next
            
        if fast == None: # edge case if len(list) == n it means delete the first node
            return head.next
        
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # slow will point to prev element of the nth_node(node to be deleted)
        return head
        
        '''
        # using two traversal
        TC -> O(2N)
        SC -> O(1)
        
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
        
        '''
            
            