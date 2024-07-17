import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import pprint
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
# MY Solution (WIN)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        res = cur = ListNode(none)
        for elements in lists:
            while elements:
                tmp.append(elements.val)
                elements = elements.next

        ordered_list = sorted(tmp)
        for val in ordered_list:
            cur.next = ListNode(val)
            cur = cur.next

        return res.next
"""

# Solved by pirority queue (heapq)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            heapq.heappush(heap, lists[i].val, i, lists[i])

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


if __name__=="__main__":
	testcase = [[1,4,5],[1,3,4],[2,6]]
	print("hello world")

	sol = Solution()
    print(sol.mergeKLists(testcase))

