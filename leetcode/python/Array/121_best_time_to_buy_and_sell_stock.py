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
# My Solution: Fail
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp_dict = {}
        for idx, price in enumerate(prices):
            tmp_dict[price] = idx

        tmp_dict = dict(sorted(tmp_dict.items()))

        weight = list(tmp_dict.keys())
        left = 0
        right = len(tmp_dict) - 1

        while left < right:
            left_val = weight[left]
            right_val = weight[right]
            print("[{}] {} / [{}] {}".format(left, left_val, right, right_val))

            if tmp_dict[left_val] > tmp_dict[right_val]:
                if weight[left + 1] - weight[left] < weight[right] - weight[right - 1]:
                    left += 1
                else:
                    right -= 1
            else:
                return right_val - left_val

        return 0

# 저점과 현재 값과 의 차이 계산 방식 (주가를 그래프로 시각화 해 생각)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = 9999999

        for price in prices:
            if low_price > price:
                low_price = price
            else:
                profit = price - low_price
                print(profit)
                if max_profit < profit:
                    max_profit = profit
        return max_profit
"""     

# WIN
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


if __name__=="__main__":
    # testcase = [4,1,2]
    testcase = [7,6,4,3,1]

    sol = Solution()
    print(sol.maxProfit(testcase))
