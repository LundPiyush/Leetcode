"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverseLinkedList(self,head):
        cur= head
        prev,next_p = None, None
        while cur:
            next_p = cur.next
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
        
    def reverse(self,head, k):
        # Code here
        
        temp = head
        prev,next_node = None,None
        while temp!=None:
            kth_node = self.getKthNode(temp,k)
            if kth_node == None:
                if prev:
                    prev.next = self.reverseLinkedList(temp)
                    break
            
            next_node = kth_node.next
            kth_node.next = None
            self.reverseLinkedList(temp)
            if temp == head:
                head = kth_node
            else:
                prev.next = kth_node
            prev = temp
            temp = next_node
        return head

#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends