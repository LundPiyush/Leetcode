# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        a = headA
        b = headB
        
        while a != b:
            a = headB if a == None else a.next 
            b = headA if b == None else b.next 
        return a
        
        
        
        
        
        
        
        st = set()
        while headB:
            st.add(headB)
            headB = headB.next
        
        while headA:
            if headA in st:
                return headA
            headA= headA.next
        return None
        
        
        '''
        while headB!=None:
            temp = headA
            while temp!=None:
                if headB == temp:
                    return headB
                temp = temp.next
            headB = headB.next
        return None
        '''