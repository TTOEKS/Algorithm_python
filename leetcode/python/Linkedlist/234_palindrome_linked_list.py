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
My Solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        deq = collections.deque()

        node = head
        while node is not None:
            deq.append(node.val)
            node = node.next

        while len(deq) > 1:
            if deq.pop() != deq.popleft():
                return False

        return True
"""
"""
다중 할당 In python
파이썬에는 다중 할당이라는 2개 이상의 값을 2개 이상의 변수에 동시 할당이 가능하다

파이썬의 특징으로 불변 객체라는 개념이 존재함
  * rev = slow시, rev와 slow가 모두 같은 객체를 참조하는 것
  * 문자와 숫자는 파이썬에서 불변 객체에 해당됨
    ex) a = 5, b = 5 인 경우 id(5) == id(a) == id(b)
    a와 b모두 파이썬의 불변 객체인 정수 5를 참조하기 때문

  * 이와 같은 특성으로 인해 리스트 자료형에서는 조심해야 함
    * 리스트 내부의 값이 불변이 아니고 가변이기 때문
"""

# Solved with runner : WIN
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev


if __name__=="__main__":
	testcase = [1,2,2,1]

	print("hello world")

	sol = Solution()
	print(sol)
