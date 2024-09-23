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

# My solution: Time exceed (Pointer 한개)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()

        for greed in g:
            if not s:
                break
            for idx in range(len(s)):
                if greed <= s[idx]:
                    res += 1 
                    del(s[idx])
                    break

        return res

# Book solution: greedy (Pointer 2개)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i

# Book solution: binary search
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0

        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result

# Leetcode solution #1
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1

        return count

# Leetcode solution #2
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        content = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                content += 1
            j += 1
        
        return content




if __name__=="__main__":
    testcase1 = [1,2,3]
    testcase2 = [3]
    print("hello world")

    sol = Solution()
    print(sol.findContentChildren(testcase1, testcase2))
