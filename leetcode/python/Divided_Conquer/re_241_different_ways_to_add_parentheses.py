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

# Book solution: divided conquer
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + str(op) + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]
        results = []
        for idx, expr in enumerate(expression):
            if expr in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                results.extend(compute(left, right, expr))
        return results

# Leetcode solution
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = '+-*'
        for c in operators:
            if c in expression:
                break
        else:
            return [int(expression)]
        res = []
        n = len(expression)
        for i in range(n):
            if expression[i] in operators:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            res.append(l+r)
                        elif expression[i] == '-':
                            res.append(l-r)
                        elif expression[i] == '*':
                            res.append(l*r)
        return res

if __name__=="__main__":
    # testcase = "2-1-1"
    testcase = "2*3-4*5"
    print("hello world")

    print("testcase: ", testcase)
    sol = Solution()
    print(sol.diffWaysToCompute(testcase))
