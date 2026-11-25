import heapq
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, idx, node) for idx, node in enumerate(lists) if node is not None]
        heapq.heapify(heap)

        head = None
        tail = None

        while heap:
            _, idx, node = heap[0]
            if node.next is not None:
                heapq.heapreplace(heap, (node.next.val, idx, node.next))
            else:
                heapq.heappop(heap)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        return head