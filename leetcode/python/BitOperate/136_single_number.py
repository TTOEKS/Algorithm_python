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
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        for val, cnt in count.items():
            if cnt == 1:
                return val

        return -1

# Solved by XOR (best)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result
"""

if __name__=="__main__":
	testcase = [4,1,2,1,2]
	print("hello world")

	sol = Solution()
	print(sol.singleNumber(testcase))
