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
# My Soltuion FAIL: This algorithm can remove word which possible subting by clear function
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = []
        res = 0
        for char in s:
            if char in sub_string:
                if (res < len(sub_string)):
                    res = len(sub_string)
                    sub_string.clear()
                else:
                    sub_string.append(char)
        return res

# My Solution: saw two points hint (start, end)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 1
        if len(s) == 0:
            return 0
    
        max_len = 1
        while len(s) > end and start < end:
            print("{} - {}".format(start, end))
            if s[end] in s[start:end]:
                start += 1
                if s[end] == s[start - 1]:
                    end += 1
            else:
                max_len = max(max_len, end - start + 1)
                end += 1
        return max_len

"""

# Solved window slicing and two points
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        hash_map = {}
        max_length = 0

        for end in range(len(s)):
            # skip to next
            if s[end] in hash_map and hash_map[s[end]] >= start:
                start = hash_map[s[end]] + 1

            hash_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
