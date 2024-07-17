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
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            print("VAL: ", self.val)
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root

# Best solution (DFS)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cnt = 0
        def dfs(root):
            if root:
                dfs(root.right)
                root.val = self.cnt = self.cnt + root.val 
                dfs(root.left)
        dfs(root)
        return root

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
