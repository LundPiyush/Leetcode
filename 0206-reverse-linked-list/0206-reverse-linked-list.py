# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nexxt = None
        while head:
            nexxt = head.next #move next to ahead of head
            head.next = prev # broke the link
            prev = head     # move prev ahead by 1
            head = nexxt # move head ahead by 1
        return prev
    