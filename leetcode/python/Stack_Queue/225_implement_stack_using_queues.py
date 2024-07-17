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
class MyStack:
    def __init__(self):
        self.queue:list = []
        # self.temp_queue:list = []
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        res = 0
        self.length -= 1
#        for i in range(self.length):
#            self.temp_queue.append(self.queue.pop(0))
#        res = self.queue.pop(0)
#        self.queue = self.temp_queue
        res = self.queue.pop()
        return res

    def top(self) -> int:
        return self.queue[self.length - 1]
        

    def empty(self) -> bool:
        return self.length == 0
"""

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__=="__main__":
    # `testcase = []
    cmds = ["MyStack","push","push","top","pop","empty"]
    args = [[],[1],[2],[],[],[]]


    print("hello world")

    sol = Solution()
    print(sol)
