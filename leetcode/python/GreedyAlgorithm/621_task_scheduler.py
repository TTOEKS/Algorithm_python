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
from time import sleep


"""
# My solution: priority queue (루프 탍출 조건 고민 필요)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        heap = []
        idle_queue = collections.deque()
        exist_map = collections.deque()
        result = 0

        for data, cnt in count.items():
            heapq.heappush(heap, (-cnt, data))

        for _ in range(n):
            # WTF?
            exist_map.append((0, "idle"))

        cnt = 0
        while heap or idle_queue:
            # WTF?
            if not heap and exist_map == idle_queue:
                break
            
            if heap:
                idle_queue.append(heapq.heappop(heap))
            else:
                idle_queue.append((0, "idle"))

            if len(idle_queue) == n + 1:
                idled_data = idle_queue.popleft()
                if idled_data[0] < -1:
                    heapq.heappush(heap, (idled_data[0] + 1, idled_data[1]))

            result += 1

        return result - n


# solved by book (priority queue, greedy)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 최대 힙 효과를 내기 위해 가장 많은 수를 가진 item 추출
            for tasks, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                # Counter 추출 함수
                counter.subtract(tasks)

                # Hack: 빈 Counter를 더해서 0이하인 아이템 삭제
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result
"""
# Solved by someone who correct submissioned at leetcode
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_set = Counter(tasks)
        pq = [-x for x in freq_set.values()]
        heapq.heapify(pq)
        
        q = collections.deque()
        timer = 0

        while pq or q:
            timer += 1
            if pq:
                rem = 1 + heapq.heappop(pq)
                if rem:
                    q.append([rem, n+timer])
            
            if q and q[0][1] <= timer:
                heapq.heappush(pq, q[0][0])
                q.popleft()
        
        return timer


if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	# print(sol.leastInterval(["A","A","A","B","B","B"], 3))
	print(sol.leastInterval(["A","A"], 2))
