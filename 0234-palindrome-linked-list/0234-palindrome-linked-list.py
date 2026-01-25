# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        if head.next is None:
            return True

        listL = []
        listR = []

        slow = head
        fast = head
        curr = head
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count +=2
        # if fast.next:
        #     count += 1

        i = 0
        while curr:
            if i < count//2:
                listL.append(curr.val)
            else:
                listR.append(curr.val)
            i += 1
            curr = curr.next
        listR.reverse()
        return listL == listR

 

        