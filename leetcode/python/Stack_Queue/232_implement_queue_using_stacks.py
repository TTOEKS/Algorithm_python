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
# My Solution
class MyQueue:

    def __init__(self):
        self.stack = []
        self.length = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1
        

    def pop(self) -> int:
        tmp_stack = []
        res = 0
        self.length -= 1

        for _ in range(self.length):
            tmp_stack.append(self.stack.pop())
        res = self.stack.pop()

        for _ in range(self.length):
            self.stack.append(tmp_stack.pop())

        return res

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return self.length == 0
"""

# WIN
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return self.input == [] and self.output == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
