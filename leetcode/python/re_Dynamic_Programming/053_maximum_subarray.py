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


# My solution: Two pointer (fail)
# Two pointer is useful with sorted array
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            nums_sum = sum(nums[left:right])
            move_left = sum(nums[left + 1: right]) if left + 1 < right else 0
            move_right = sum(nums[left: right - 1]) if left < right - 1 else 0

            if (move_right < move_left) and (nums_sum < move_left):
                left += 1
            elif (move_left < move_right) and (nums_sum < move_right):
                right -= 1
            else:
                return nums[left:right]

        return None


# Book solution: memoization
# 배열에 이전 값과 더한 값을 저장한 후, 가장 큰 값을 출력
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

        return max(nums)

# Book solution: Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__=="__main__":
    testcase = [-2,1,-3,4,-1,2,1,-5,4]
    print("hello world")

    print("testcase: ", testcase)
    sol = Solution()
    print(sol.maxSubArray(testcase))
