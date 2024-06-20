import sys
import heapq
import math 

N, X, T = map(int, sys.stdin.readline().split())

def dijk(start, end, graph):
    dist = [math.inf for _ in range(N+2)]
    edges = []

    dist[start] = 0
    heapq.heappush(edges, (dist[start], start))

    while edges:
        cost, pos = heapq.heappop(edges)
        for p, c in graph[pos]:
            c += cost
            if dist[p] > c:
                dist[p] = c
                heapq.heappush(edges, (c, p))
    return dist[end]

graph = [[] for _ in range(N+2)]
graph_bak = [[] for _ in range(N+2)]

while X:
    X -= 1
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph_bak[b].append((a, c))

m = 0
for idx in range(N):
    m = max(m, dijk(idx+1, T, graph) + dijk(T, idx+1, graph))

print(m)


