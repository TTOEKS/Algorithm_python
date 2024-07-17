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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            
            return max(left, right) + 1

        return dfs (root) != -1 


# Solved by recursive
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
