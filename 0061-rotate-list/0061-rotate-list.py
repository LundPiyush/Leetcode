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
        new_tail = head # this will find last node in the return linked list
        while end>1:
            new_tail = new_tail.next
            end -= 1
    # breaking last node link and pointing to NULL
        head = new_tail.next
        new_tail.next = None


        return head 