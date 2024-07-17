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

# Solve by DFS, Backtracking
class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


# Best solved
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        def helper(node, parent):
            if not node:
                return 0

            left = helper(node.left, node)
            right = helper(node.right, node)
            
            self.res = max(self.res, left+right)
            if parent and node.val == parent.val:
                return max(left, right) + 1
            else:
                return 0

        helper(root, None)
        return self.res


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
