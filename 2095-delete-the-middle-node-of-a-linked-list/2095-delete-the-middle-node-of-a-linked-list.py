# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
            
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1
        
        midR = count//2 - 1
        prev = head

        for _ in range(midR):
            prev = prev.next
        
        delete_node = prev.next
        prev.next = delete_node.next

        return head
        