/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    fast = mid = head
    prev = null
    
    while(fast && fast.next){
        fast = fast.next.next
        prev= mid
        mid = mid.next      
    }
    if(fast == mid){
        return null
       }
    prev.next = mid.next
    mid.next = null
    return head
    
};