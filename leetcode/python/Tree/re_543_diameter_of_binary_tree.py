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
    longest: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Leaf node
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # Plus 2 for left, right leaf node -1
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest



if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
