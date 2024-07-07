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
# My Solution: WIN
class Solution:
    # s: () [] {}
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                bucket = stack.pop()
                if c == ')' and bucket != '(':
                    return False
                elif c == ']' and bucket != '[':
                    return False
                elif c == '}' and bucket != '{':
                    return False

        return len(stack) == 0
"""
class Solution:
    # s: () [] {}
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0



if __name__=="__main__":
	testcase = "(([]]){}"
	print("hello world")

	sol = Solution()
	print(sol.isValid(testcase))
