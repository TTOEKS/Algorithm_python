import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import pprint
import copy
from typing import *

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        result = []
        curr = intervals[0]
        N = len(intervals)
        for i in range(1, N):
            if curr[1] >= intervals[i][0]:
                curr[1] = max(intervals[i][1], curr[1])
            else:
                result.append(curr)
                curr = intervals[i]
        result.append(curr)
                
        return result





# My solution: Failed
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_sort(left, right):
            res = []
            while left and right:
                if left[0] < right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))

            while left:
                res.append(left.pop(0))
            while right:
                res.append(right.pop(0))

            return res

        tmp = copy.deepcopy(intervals)

        while True:
            if len(tmp) == 1:
                break

            merge_tmp = []
            for i in range(0, len(tmp), 2):
                if len(tmp) >= 2:
                    tmp_res = merge_sort(tmp[i], tmp[i + 1])
                else:
                    tmp_res = tmp[i]
                merge_tmp.append(tmp_res)
            tmp = merge_tmp[:]
        sort_data = tmp.pop()

        print(intervals)
        res = []
        first = -1
        second = -1

        for idx in range(len(intervals)):
            if first == -1:
                first = intervals[idx][0]

            if intervals[idx][1] == sort_data[2 * idx + 1]:
                if (idx + 1) * 2 > len(sort_data) - 1:
                    second = intervals[idx][1]
                else:
                    if intervals[idx][1] != sort_data[(idx + 1) * 2]:
                        second = intervals[idx][1]
                

            if first != -1 and second != -1:
                res.append([first, second])
                first = -1
                second = -1

        return res
"""         

# Solution by book
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []

        # 첫번째 요소 기준으로 정렬한 데이터 iternation
        for i in sorted(intervals, key=lambda x: x[0]):
            # 현재 merge에 들어간 최신 값 중 end가 새로운 요소 start보다 큰 경우
            if merge and i[0] <= merge[-1][1]:
                merge[-1][1] = max(merge[-1][1], i[1])
            else:
                merge += i

        return merge



# Best solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []
        cur = intervals[0]
        N = len(intervals)

        for i in range(1, N):
            if cur[1] >= intervals[i][0]:
                cur[1] = max(intervals[i][1], cur[1])
            else:
                result.append(cur)
                cur = intervals[i]
        result.append(cur)

        return result


if __name__=="__main__":
    # 1, 2, 3, 6, 8, 10, 15, 18
    testcase = [[1,3],[2,6],[8,10],[15,18]]
    testcase = [[1, 4], [4, 5]]
    print("hello world")

    sol = Solution()
    print(sol.merge(testcase))
