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
# My solution: Fail -> May be i would use two pointer instead queue
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer_sheet = collections.Counter(t)
        current = collections.defaultdict(int)
        queue = collections.deque()
        res = ""

        for c in s:
            if c in answer_sheet.keys():
                if current[c] == answer_sheet[c]:
                    while queue:
                        data = queue.popleft()
                        if data == c:
                            current[c] -= 1
                            while queue and queue[0] not in answer_sheet.keys():
                                queue.popleft()
                            break
                        else:
                            if data in current:
                                current[data] -= 1
                queue.append(c)
                current[c] += 1
                if current == answer_sheet:
                    if res == "" or len(queue) < len(res) :
                        res = "".join(queue)
                    current[queue.popleft()] -= 1
                    while queue and queue[0] not in answer_sheet.keys():
                        queue.popleft()
            else:
                if len(queue) != 0:
                    queue.append(c)
        return res
"""

# Solution by book (brouteforce while increase window range)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_lst: List):
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ""

        window_size = len(t)
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left: left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr

        return ''


# WIN
# Solved by book (two pointer, window-slicing optimized)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]


# Solved by book (optimizing two pointer with Counter)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start:end] if end - start <= len(s) else ""




if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol.minWindow("acbbaca", "aba"))
