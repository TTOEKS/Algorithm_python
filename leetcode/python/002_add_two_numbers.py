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

# I think this problem have to referecned solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
# with convert variable type
class Solution:
    def reverse_list(self, linkedlist: ListNode):
        node, prev = linkedlist, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: ListNode) -> List:
        list: List = []

        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverse_list(l1))
        b = self.toList(self.reverse_list(l2))

        resultStr = int(''.join(str(e) for e in a)) + int("".join(str(e) for e in b))
        return self.toReversedLinkedList(str(resultStr))
"""     

# Solved by 전가산기 (logic gate) (WIN)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # divmod function return tuple which divieded (val, rest)
            carry, val = divmod(sum + carry, 10)
            print(carry, val)
            head.next = ListNode(val)
            head = head.next
        
        return root.next

if __name__=="__main__":
    testcase = [2, 4, 3]
    testcase2 = [5, 6, 4]

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
    res = sol.addTwoNumbers(case1, case2)
    while res != None:
        print(res.val)
        res = res.next
