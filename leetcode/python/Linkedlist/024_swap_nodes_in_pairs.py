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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = tmp = ListNode(0)
        queue = []
        cnt = 0

        if head == None:
            return head

        pos = head
        while pos != None:
            queue.append(pos.val)
            cnt += 1
            if cnt % 2 == 0:
                while len(queue) != 0:
                    tmp.next = ListNode(queue.pop())
                    tmp = tmp.next
            pos = pos.next

        
        while len(queue) != 0:
            tmp.next = ListNode(queue.pop())
            tmp = tmp.next

        return res.next

# Value switch
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head


# Swap with loop
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head.next
            prev = prev.next.next

        return root.next



"""
# Swap with recursive
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("FUNC: {}".format(head.val))
        if head and head.next:
            p = head.next
            head.next =  self.swapPairs(p.next)
            print("AFTER RECUR: {}".format(head.next.val))
            p.next = head
            return p

        return head


if __name__=="__main__":
    testcase = [1, 2, 3, 4, 6 ]
    print("hello world")

    case = ListNode(testcase[0])
    pos = case
    for i in range(1, len(testcase)):
        tmp = ListNode(testcase[i])
        pos.next = tmp
        pos = pos.next
    
    sol = Solution()
    res = sol.swapPairs(case)
    while res != None:
        print(res.val)
        res = res.next

