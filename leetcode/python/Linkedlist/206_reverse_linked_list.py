from _typeshed import NoneType
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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
# My Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        stack = []

        pos = head
        while pos:
            stack.append(pos.val)
            pos = pos.next

        res = ListNode(stack.pop())
        pos = res
        while stack:
            tmp = ListNode(stack.pop())
            pos.next = tmp
            pos = pos.next

        return res

# using recursive (need more think about algorithm)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

"""     

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        """
        1, 2, 3, 4, 5
        R1) next=2, node.next=none, prev=1, node=2
        R2) next=3, node.next=1,    prev=2, node=3
        """
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

if __name__=="__main__":
    testcase = [1,2,3,4,5]

    case1 = ListNode(testcase[0])
    pos = case1
    for i in range(1, len(testcase)):
        tmp = ListNode(testcase[i])
        pos.next = tmp
        pos = pos.next

    sol = Solution()
    res = sol.reverseList(case1)
    while res:
        print(res.val)
        res = res.next
