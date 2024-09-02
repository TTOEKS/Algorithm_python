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

# My solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')

# Best solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n % 2)
            n >>= 1
        return count


# Bit operation by book
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol.hammingWeight(2147483645))
