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
# My Solution
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or (left == right):
            return head

        cur = head
        stack = []
        cnt = 1
        tmp_head = None

        while cur:
            if cnt == left:
                stack.append(cur.val)
                tmp_head = cur
            
            if left < cnt < right:
                stack.append(cur.val)

            if cnt == right:
                stack.append(cur.val)
                if tmp_head:
                    while len(stack):
                        tmp_head.val = stack.pop()
                        tmp_head = tmp_head.next
                break
            cur = cur.next
            cnt += 1
    
        return head
"""

# 책의 풀이 이해 필요 WIN
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 동작 방식 이해 필요
        for _ in range(right - left):
            # tmp, start.next, end.next = start.next, end.next, end.next.next
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next

if __name__=="__main__":
    testcase = [1, 2, 3, 4, 5]
    print("hello world")

    case = tmp = ListNode(testcase[0])
    for i in range(1, len(testcase)):
        tmp.next = ListNode(testcase[i])
        tmp = tmp.next

    sol = Solution()
    res = sol.reverseBetween(case,2, 4)
    while res != None:
        print(res.val)
        res = res.next

