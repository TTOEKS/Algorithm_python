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


# My Soltuion
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(numbers, target, left, right):
            if left > right:
                return -1

            mid = left + (right - left) // 2
            if numbers[mid] > target:
                return binary_search(numbers, target, left, mid - 1)
            elif numbers[mid] < target:
                return binary_search(numbers, target, mid + 1, right)
            else:
                return mid

        for idx, val in enumerate(numbers):
            expected = target - val
            index = binary_search(numbers, expected, idx + 1, len(numbers) - 1)
            if index != -1:
                return [idx + 1, index + 1]

# Binary Serach in Book
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > expected:
                    right = mid - 1
                elif numbers[mid] < expected:
                    left = mid + 1
                else:
                    return [k + 1, mid + 1]

# Two pointer (SECOND)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

# bisect module with slicing
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]

            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2


# bisect module and delete slicing (FIRST)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


if __name__=="__main__":
    # testcase = [2,7,11,15]
    testcase = [-1, 0]
    print("hello world")

    sol = Solution()
    print(sol.twoSum(testcase, -1)) 
