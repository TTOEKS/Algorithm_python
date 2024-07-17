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

# My Solution
class Solution:
    sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            if node.val >= low and node.val <= high:
                self.sum += node.val
            dfs(node.right)
        dfs(root)
        return self.sum

# Solved by Recursive DFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) \
            + self.rangeSumBST(root.left, low, high)\
            + self.rangeSumBST(root.right, low, high)


# Solved by DFS using stack
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

                if low <= node.val <=  high:
                    sum += node.val
        return sum


# Solved by BFS using queue
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)

                if low <= node.val <=  high:
                    sum += node.val
        return sum



        
if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
