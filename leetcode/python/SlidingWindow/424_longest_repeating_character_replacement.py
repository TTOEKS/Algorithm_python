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
# My solution: Two pointer: FAIL
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        current_char = s[0]
        num_missing = 0

        res = 0
        while end < len(s) - 1:
            end += 1
            if s[end] != current_char:
                num_missing += 1

            if num_missing > k:
                res = max(res, end - start)
                while start < (end or len(s) - 1):
                    start += 1
                    if s[start] != current_char:
                        current_char = s[start]
                        end = start
                        num_missing = 0
                        break

        if num_missing <= k:
            res = max(res, end - start + 1)

        return res
"""

# Solved by book: two pointer, counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left





if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol.characterReplacement("ABBB", 2))
