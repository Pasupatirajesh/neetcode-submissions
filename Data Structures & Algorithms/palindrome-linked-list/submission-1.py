# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        right = reverse_list(slow)
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
