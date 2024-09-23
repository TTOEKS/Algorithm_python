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
# Book solution: 파보나치 수열 (Time exceeded)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Book solution: Memoization
class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
"""

# Leetcode solution: Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        steps=[0 for i in range(n)]
        print(steps)
        print()
        steps[0]=1
        print(steps)
        print()
        if n==1: return 1
        if n==2: return 2
        steps[1]=2
        print(steps)
        print()
        for i in range(2,n):
            print(steps)
            steps[i]=steps[i-1]+steps[i-2]
        print(steps)
        print()
        return steps[-1]



if __name__=="__main__":
	testcase = []
	print("hello world")

	# print("testcase: ", testcase)
	sol = Solution()
	print(sol.climbStairs(7))
