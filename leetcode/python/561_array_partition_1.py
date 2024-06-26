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
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i + 1])

        return res

### WIN
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        for i in range(0, len(nums), 2):
            res += nums[i]

        return res

"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__=="__main__":
	testcase = [1,4,3,2]
	print("hello world")

	sol = Solution()
	print(sol.arrayPairSum(testcase))
