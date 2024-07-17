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


# 문제를 잘 이해하지 못했음
"""
bcabc -> abc
  - 중복 문자를 제거하고 사전적으로 abc가 먼저 나옴

ebcabc -> ebca
  - 중복 문자를 제거하고 사전적으로 ebcad가 먼저 나옴 (e는 중복 문자가 없음)

ebcabce -> abce
  - 중복 문자를 제거하고 사전적으로 abce가 먼저 나옴 

중복 값을 허용하지 않는 set 자료구조를 사용
"""

"""
# Using Set
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print("SUFFIX: ", suffix)
            if set(s) == set(suffix):
                print("EQUAL {} - {}".format(set(s), set(suffix)))
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ''
"""

# Using stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1 
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)


if __name__=="__main__":
	testcase = "cbacdcdc"
	print("hello world")

	sol = Solution()
	print(sol.removeDuplicateLetters(testcase))
