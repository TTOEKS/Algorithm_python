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


# Using STACK
"""
Stack의 용도
  * 따듯해지기 위해 더 기다려야 하는 날짜를 기록
  * 현재 온도보다 Stack에 기록된 날의 온도가 더 낮으면
  * 현재 날짜와 기록된 날짜를 빼서 기다려야 하는 일수를 기록
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            print("ANSWER: ", answer)
            print("STACK: ", stack)

            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            print()


        return answer

if __name__=="__main__":
    testcase = [73,74,75,71,69,72,76,73]
    print("hello world")

    sol = Solution()
    print(sol.dailyTemperatures(testcase))
