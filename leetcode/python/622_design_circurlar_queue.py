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

"""
# My Solution (WIN)
class MyCircularQueue:
    def __init__(self, k: int):
        self.max_num = k
        self.stack = []
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.stack.append(value)
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.stack.pop(0)
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.length <= 0:
            return -1
        return self.stack[0]

    def Rear(self) -> int:
        if self.length <= 0:
            return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max_num

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
"""

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxsize = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxsize
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return True

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.rear] is not None


if __name__=="__main__":
    testcase = []
    print("hello world")

    sol = Solution()
    print(sol)
