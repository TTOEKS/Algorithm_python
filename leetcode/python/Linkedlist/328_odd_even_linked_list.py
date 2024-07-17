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
        if head is None or head.next is None:
            return head

        odd= head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head

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
