# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_grp_end = dummy
        while True:
            kth_node = prev_grp_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            group_start = prev_grp_end.next
            next_group_start = kth_node.next

            prev, cur = None, group_start
            for _ in range(k):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            prev_grp_end.next = prev
            group_start.next = next_group_start

            prev_grp_end = group_start
        return dummy.next
