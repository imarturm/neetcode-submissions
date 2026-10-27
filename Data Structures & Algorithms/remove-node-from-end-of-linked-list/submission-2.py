# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        index = length - n - 1
        if index == -1:
            return head.next

        cur = head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next if cur.next else None
        return head