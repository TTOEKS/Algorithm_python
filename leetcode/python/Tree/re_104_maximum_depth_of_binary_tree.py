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

# best solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        depth = 1
        queue = collections.deque()

        queue.append((root, 1))

        while queue:
            tmpNode, level = queue.popleft()

            depth = max(depth, level)

            if tmpNode.left:
                queue.append((tmpNode.left, level + 1))
                
            if tmpNode.right:
                queue.append((tmpNode.right, level + 1))

        return depth


# Reference book (LINE 13)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        depth = 0
        queue = []

        queue.append(root)
        while queue:
            depth += 1

            # Root number of child nodes
            for _ in range(len(queue)):
                tmpNode = queue.pop(0)
    
                if tmpNode.left:
                    queue.append(tmpNode.left)
                
                if tmpNode.right:
                    queue.append(tmpNode.right)
    
        return depth



if __name__=="__main__":
	testcase = [3,9,20,null,null,15,7]
	print("hello world")

	sol = Solution()
	print(sol)
