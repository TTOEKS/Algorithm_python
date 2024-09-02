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
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while end > start:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return -1

# Solved by recursive binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid  
            else:
                return -1
        return binary_search(0, len(nums) - 1)

"""

# Solved by loop binary search (book)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

# Solved by bisect 모듈 (이진 검색 모듈)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index <= len(nums) and nums[index] == target:
            return index
        else:
            return -1


# 이진 검색을 사용하지 않는 index 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


if __name__=="__main__":
	testcase = [-1,0,3,5,9,12]
	print("hello world")

	sol = Solution()
	print(sol.search(testcase, 9))
