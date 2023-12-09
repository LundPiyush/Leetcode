# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
    # calculating length
        temp = head
        length = 1
        while temp.next != None:
            length += 1
            temp = temp.next
    # link last node to first node
        temp.next = head
        k = k % length  # when k is more than length of list
        end = length - k  # to get end of the list
        while end:
            temp = temp.next
            end -= 1
    # breaking last node link and pointing to NULL
        head = temp.next
        temp.next = None


        return head 