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

# My solution (FAIL)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(numbers, target, left, right):
            if left > right:
                return False
            mid = left + (right - left) // 2

            if target < numbers[mid]:
                return binary_search(numbers, target, left, mid - 1)
            elif target > numbers[mid]:
                return binary_search(numbers, target, mid + 1, right)
            else:
                return True

        col = 0
        for idx in range(len(matrix[0])):
            if target == matrix[0][idx]:
                return True

            if target > matrix[0][idx]:
                col = idx
            else:
                break

        print(col)
        tmp = []
        for idx in range(len(matrix)):
            tmp.append(matrix[idx][col])
        print(tmp)

        return binary_search(tmp, target, 0, len(tmp) - 1)


# 규칙을 찾았어야 함 (작으면 왼 / 크면 아래)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


if __name__=="__main__":
    # testcase = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    testcase = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    print("hello world")

    sol = Solution()
    print(sol.searchMatrix(testcase, 19))
