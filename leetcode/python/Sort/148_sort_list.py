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

# My solution: Failed to implemented merge sort function
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(elements):
            result = []
            division = 1

            while division < len(elements):
                tmp_res = []
                tmp_list = []
                while elements:
                    tmp = []
                    for _ in range(division):
                        if elements:
                            tmp.append(elements.pop(0))
                    tmp_list.append(tmp)

                while len(tmp_list) >= 2:
                    left = tmp_list.pop(0)
                    right = tmp_list.pop(0)

                    while left and right:
                        l_data = left.pop(0)
                        r_data = right.pop(0)
                        
                        if l_data < r_data:
                            result.append(l_data)
                            result.append(r_data)
                        else:
                            result.append(r_data)
                            result.append(l_data)

                    while left:
                        result.append(left.pop(0))

                    while right:
                        result.append(right.pop(0))

                while tmp_list:
                    tmp = tmp_list.pop()
                    result.append(tmp.pop(0))

                elements = result
                division *= 2
            
        tmp_list = []
        root = result = ListNode(None)
        cur = head

        while cur:
            tmp_list.append(cur.val)
            cur = cur.next


        print(tmp_list)
        merge_sort(tmp_list)
        print(tmp_list)

        for data in tmp_list:
            result.next = ListNode(data)
            result = result.next

        return root.next



# 파이선 내장 함수 사용
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_list = []
        root = result = ListNode(None)
        cur = head

        while cur:
            tmp_list.append(cur.val)
            cur = cur.next

        tmp_list.sort()

        for data in tmp_list:
            result.next = ListNode(data)
            result = result.next

        return root.next


# Solved by merge sort (find middle value with runner)
# Best solution
class Solution:
    def mergeTowLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTowLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTowLists(l1, l2)

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
