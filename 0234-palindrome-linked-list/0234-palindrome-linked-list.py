# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #TC: O(n)   SC: O(n)
        # if not head or not head.next:
        #     return True

        # listLL = []
        # curr = head
        # while curr:
        #     listLL.append(curr.val)
        #     curr = curr.next
        
        # return listLL == listLL[::-1]

        if not head or not head.next:
            return True
        
        slow = fast = head

        #finding the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the right part after mid point:
        curr = slow
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # matching the right and left part
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
        



            


 

        