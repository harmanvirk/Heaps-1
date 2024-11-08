#TC = O(n logk) | SC = O(k)

from heapq import heappush as push
from heapq import heappop as pop
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lessThan = lambda x, y: x.val < y.val
        ListNode.__lt__ = lessThan

        minHeapK = []

        dummyHead = ListNode(-1)
        cursorNode = dummyHead

        for i in range(len(lists)):
            currHead = lists[i]
            if (currHead != None):
                push(minHeapK, currHead)

        while (len(minHeapK) > 0):

            minNode = pop(minHeapK)

            cursorNode.next = minNode
            if (minNode.next != None):
                push(minHeapK, minNode.next)

            cursorNode = minNode

        return dummyHead.next