# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        listLL = []
        curr = head
        while curr:
            listLL.append(curr.val)
            curr = curr.next
        
        return listLL == listLL[::-1]


            


 

        