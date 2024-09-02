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

# My solution: Time exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start, end = 0, k
        result = []
        for _ in range(len(nums) + 1 - k):
            
            result.append(max(nums[start:end]))
            start += 1
            end += 1

        return result


# Solved by broute force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

# Solved by queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        windows = collections.deque(nums[0:k - 1])
        for i in range(k - 1, len(nums)):
            windows.append(nums[i])
            print(windows)
            res.append(max(windows))
            windows.popleft()

        return res

# Solved by obtimized queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [] 
        windows = collections.deque()
        current_max = float('-inf')

        for i, v in enumerate(nums):
            windows.append(v)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(windows)
            elif v > current_max:
                current_max = v

            result.append(current_max)

            if current_max == windows.popleft():
                current_max = float('-inf')

        return result



# Solved by heapq
class Solution(object):
    def add_to_deque(self, dq, nums ,i):
        while len(dq) and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        return 

    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        for i in range(k):
            self.add_to_dq(dq, nums, i)

        result, start, end = [nums[dq[0]]], 1, k

        while end < len(nums):
            self.add_to_deque(dq, nums, end)
            while True:
                if dq[0] >= start:
                    result.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start, end = start + 1, end + 1
        return result



# Best solution: remainint queue only bigger than latest input value
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        q = collections.deque()

        for r in range(len(nums)):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

            if r + 1 >= k:
                res.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return res




if __name__=="__main__":
	testcase = [1,3,-1,-3,5,3,6,7]
	print("hello world")

	sol = Solution()
	print(sol.maxSlidingWindow(testcase, 3))
