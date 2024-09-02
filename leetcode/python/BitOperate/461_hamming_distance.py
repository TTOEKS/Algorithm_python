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
# My solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        return bin(res).count('1')
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()


if __name__=="__main__":
	print("hello world")

	sol = Solution()
	print(sol.hammingDistance(1, 4))
