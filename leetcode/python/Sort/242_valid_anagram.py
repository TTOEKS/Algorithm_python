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


# My solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(map(str, s))
        b = list(map(str, t))

        a.sort(), b.sort()
        return a == b

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(map(str, s)) == collections.Counter(map(str, t))

# Book solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(b)


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
