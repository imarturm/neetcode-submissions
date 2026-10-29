# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next
