# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        tail = head
        n = 1
        while tail.next !=None:
            tail = tail.next
            n = n + 1
        k = k%n
        tail.next = head
        count = n - k
        ans = head
        while count>1:
            count = count-1
            ans = ans.next
        head = ans.next
        ans.next = None
        return head