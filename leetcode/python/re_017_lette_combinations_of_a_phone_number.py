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
class Solution:
    phone_alpha = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }


    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return 

            for i in range(index, len(digits)):
                for j in self.phone_alpha[digits[i]]:
                    dfs(i + 1, path + j)


        if not digits:
            return []

        result = []
        dfs(0, "")

        return result


"""    
# BEST SOLVED 1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = digit_to_chars[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
# BEST SOLVED 2
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
        result = []
        def recurse(i, s):
            if i == len(digits):
                result.append(s)
                return

            for l in mapping[digits[i]]:
                recurse(i + 1, s + l)

        if digits:
            recurse(0, "")

        return result

if __name__=="__main__":
    testcase = "23"
    print("hello world")

    sol = Solution()
    print(sol.letterCombinations(testcase))
