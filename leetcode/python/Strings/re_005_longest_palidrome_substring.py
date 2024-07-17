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

# 제제공된 문자열에서 가장 긴 팰린드롬 부분 문자열을 출력

class Solution:
    def longestPalindrome(self, s: str) -> str:
         # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1

            return s[left + 1: right - 1]
        
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""

        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key = len)
        
        return result


if __name__=="__main__":
    testcase = "babad"

    sol = Solution()
    print(sol.longestPalindrome(testcase))

