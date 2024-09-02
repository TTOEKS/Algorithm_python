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

# Solved by book
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        pivot = nums.index(min(nums))
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1


if __name__=="__main__":
	testcase = [4,5,6,7,0,1,2]
	print("hello world")

	sol = Solution()
	print(sol.search(testcase, 0))
