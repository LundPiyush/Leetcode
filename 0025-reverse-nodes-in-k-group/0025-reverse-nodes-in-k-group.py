# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        cur= head
        next_p,prev= None,None
        
        while cur:
            next_p= cur.next
            cur.next = prev
            prev = cur
            cur = next_p
        return prev
    def getKthNode(self,temp,k):
        k = k-1
        while temp!=None and k>0:
            k = k-1
            temp = temp.next
        return temp
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode,nextNode = None,None

        while temp!=None:
            kthNode = self.getKthNode(temp,k)
            if kthNode == None:
                if prevNode:
                    prevNode.next = temp
                    break
            nextNode = kthNode.next
            kthNode.next = None
            self.reverseList(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
        return head
    
    
        