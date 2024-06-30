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

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenNodes = []
        res = odd_head = ListNode(None)
        cur = head

        while cur:
            if cur.val % 2 == 0:
                evenNodes.append(cur)
            else:
                if odd_head:
                    odd_head.next = cur
                    odd_head = cur
                else:
                    odd_head = cur

            cur = cur.next

        for node in evenNodes:
            odd_head.next = node
            odd_head = node

        odd_head.next = None

        return res.next

if __name__=="__main__":
    testcase = [2,1,3,5,6,4,7]
    # testcase = [1, 2, 3, 4, 5]
    print("hello world")

    case = tmp = ListNode(testcase[0])
    for i in range(1, len(testcase)):
        tmp.next = ListNode(testcase[i])
        tmp = tmp.next

    sol = Solution()
    res = sol.oddEvenList(case)
    while res != None:
        print(res.val)
        res = res.next
