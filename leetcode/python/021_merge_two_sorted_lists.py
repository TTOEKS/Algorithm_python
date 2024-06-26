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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        res_pos = res
        pos1 = list1
        pos2 = list2
        
        while pos1 is not None and pos2 is not None:
            if pos1.val <= pos2.val:
                tmp = ListNode(pos1.val)
                res_pos.next = tmp
                res_pos = res_pos.next
                pos1 = pos1.next
            else:
                tmp = ListNode(pos2.val)
                res_pos.next = tmp
                res_pos = res_pos.next
                pos2 = pos2.next

        while pos1:
            tmp = ListNode(pos1.val)
            res_pos.next = tmp
            res_pos = res_pos.next
            pos1 = pos1.next

        while pos2:
            tmp = ListNode(pos2.val)
            res_pos.next = tmp
            res_pos = res_pos.next
            pos2 = pos2.next

        res = res.next

        return res
"""

# Using recursive  (WIN)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1



if __name__=="__main__":
    testcase = [1, 2, 4]
    testcase2 = [1, 3, 4]


    case1 = ListNode(testcase[0])
    pos = case1
    for i in range(1, len(testcase)):
        tmp = ListNode(testcase[i])
        pos.next = tmp
        pos = pos.next

    case2 = ListNode(testcase2[0])
    pos = case2
    for i in range(1, len(testcase2)):
        tmp = ListNode(testcase2[i])
        pos.next = tmp
        pos = pos.next

    sol = Solution()
    res = sol.mergeTwoLists(case1, case2)
    while res != None:
        print(res.val)
        res = res.next
