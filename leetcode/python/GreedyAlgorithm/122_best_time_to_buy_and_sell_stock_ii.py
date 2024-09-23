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

# Solved by book (greedy algorithm)
# 다음 번에 오르는 경우에만 사고 파는 그리디 알고리즘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                reulst += prices[i + 1] - prices[i]
        return result

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

if __name__=="__main__":
	testcase = [7,1,5,3,6,4]
	print("hello world")

	sol = Solution()
	print(sol)
