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

"""
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,cur = head,head.next
        while cur:
            if cur.val >=prev.val:
                prev,cur = cur,cur.next
                continue
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummy.next

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution in book (BEST SOLTUION)
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next

            # 개선 점
            if head and cur.val > head.val:
                cur = parent

        return cur.next

# Solved by leetcode
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            tmp = dummy

            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
