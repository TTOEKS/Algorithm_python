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

# BEST Solved
class MyCircularDeque_deque:

    def __init__(self, k: int):
        self.k = k
        self.d = collections.deque()        

    def insertFront(self, value: int) -> bool:
        if len(self.d) == self.k:
            return False
        
        self.d.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.d) == self.k:
            return False
        
        self.d.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.d:
            self.d.popleft()
            return True
        
        return False

    def deleteLast(self) -> bool:
        if self.d:
            self.d.pop()
            return True
        
        return False
        
    def getFront(self) -> int:
        try:
            return self.d[0]
        except:
            return -1

    def getRear(self) -> int:
        try:
            return self.d[-1]
        except:
            return -1

    def isEmpty(self) -> bool:
        return len(self.d) == 0

    def isFull(self) -> bool:
        return len(self.d) == self.k

# BEST Solved 2
class ListNode :
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.maxlen, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
    """
    [node] left: None / right: <__main__.ListNode object at 0x7fe58f62b790>
    [new] left: None / right: None

    [node] left: None / right: <__main__.ListNode object at 0x7fe58f62b850>
    [new] left: <__main__.ListNode object at 0x7fe58f62b750> / right: <__main__.ListNode object at 0x7fe58f62b790>
    ------------
    [node] left: <__main__.ListNode object at 0x7fe58f62b750> / right: <__main__.ListNode object at 0x7fe58f62b790>
    [new] left: None / right: None

    [node] left: <__main__.ListNode object at 0x7fe58f62b750> / right: <__main__.ListNode object at 0x7fe58f62b950>
    [new] left: <__main__.ListNode object at 0x7fe58f62b850> / right: <__main__.ListNode object at 0x7fe58f62b790>
    ------------

    """
    
    def _add(self, node:ListNode, new:ListNode):
        right = node.right
        node.right = new
        new.left, new.right = node, right
        right.left = new
    
    def _del(self, left:ListNode):
        # 삭제 대상의 왼쪽 노드가 들어옴
        right = left.right.right
        right.left = left
        left.right = right

    def insertFront(self, value: int) -> bool:
        if self.len == self.maxlen :
            return False
        self.len += 1
        self._add(self.head, ListNode(value))        
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.len == self.maxlen :
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self) -> bool:
        if self.len == 0 :
            return False
        self.len -= 1
        self._del(self.head)
        return True
        

    def deleteLast(self) -> bool:
        if self.len == 0 :
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        

    def getFront(self) -> int:
        if self.len == 0 :
            return -1
        return self.head.right.value
        

    def getRear(self) -> int:
        if self.len == 0 :
            return -1
        return self.tail.left.value
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.maxlen
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
