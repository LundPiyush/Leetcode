# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force
        
        temp = dummy = ListNode(0)
        
        while list1!=None and list2!=None:
            if list1.val <= list2.val:
                temp.next = list1
                list1= list1.next
            else:
                temp.next = list2
                list2= list2.next
                
            temp = temp.next
        if list1!=None:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummy.next
                
            
        
        # TC - O(n1 + n2) 
        # SC - O(1)
        
        # when list1 is empty then our output will be same as list2
        if list1 == None: 
            return list2
        # when list2 is empty then our output will be same as list1
        if list2 == None: 
            return list1
        
        # pointing l1 and l2 to smallest and greatest one
        if list1.val > list2.val:
            list1,list2=list2,list1
            
        # act as head of resultant merged list
        res = list1
        
        while list1 and list2:
            temp = None
            while list1 and list1.val<=list2.val:
                temp = list1 # storing last sorted node
                list1 = list1.next
            temp.next = list2
            
            list1,list2=list2,list1
        return res
                
            
        