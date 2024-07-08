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

# My Solution: FAIL (dx, dy로 탐색을 구현하려했지만 실패)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def display_grid():
            print("#### GRID")
            for i in grid:
                for j in i:
                    print(j, end="\t")
                print()

        def dfs (i, j):
            print("[DFS] Travelling ({}, {})".format(i, j))
            if i < 0 or i >= len(grid):
                print("Found Water!")
                return
            if j < 0 or j >= len(grid[0]):
                print("Found Water!")
                return
            if grid[i][j] != '1':
                print("Found Water!")
                return

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            grid[i][j] = '0'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            """
            for i in range(4):
                dfs(i + dx[i], j + dy[i])
            """

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    print("FINISHED TRAVELLING")
                    display_grid()
                    print()
                    cnt += 1
        return cnt

"""
# Solved by DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            print("[DFS] Travelling ({}, {})".format(i, j))
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or (grid[i][j] != '1'):
                print("Found Water!")
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    print("Finish tarvelled island!")
                    print()
                    count += 1
        return count

"""



if __name__=="__main__":
    testcase = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("#### MAP")
    for i in testcase:
        for j in i:
            print(j, end="\t")
        print()


    sol = Solution()
    print(sol.numIslands(testcase))
