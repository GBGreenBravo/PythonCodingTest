# 20241230
# 1:32:34
# 1 / 8

# start->end의 최단경로를 찾는 dfs() 함수에서의 연산을 줄이기 위해,
# start->end / end->start 다익스트라를 2번 수행하고,
# 27번째 라인으로 활용하는 게 인상적이었던 문제

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(500_000)


def dfs(node, idx):
    global banned

    if banned:
        return

    if node == end:
        banned = route
        return

    for nex, added in sorted(connected[node]):
        if first_answer != visited_se[node] + added + visited_es[nex]:
            continue
        route.append(nex)
        dfs(nex, idx + 1)
        if banned:
            return
        route.pop()


def dijkstra(s, e, is_final):
    visited = [None] + [21e9 for _ in range(N)]
    if is_final:
        for ban in banned:
            visited[ban] = 0
    visited[s] = 0
    queue = [(0, s)]
    while queue:
        cost, now = heappop(queue)

        if visited[now] != cost:
            continue

        if now == e:
            return visited, cost

        for nex, added in connected[now]:
            if visited[nex] <= cost + added:
                continue
            visited[nex] = cost + added
            heappush(queue, (cost + added, nex))


N, M = map(int, input().split())
connected = [None] + [[] for _ in range(N)]
for _ in range(M):
    aa, bb, cc = map(int, input().split())
    connected[aa].append((bb, cc))
    connected[bb].append((aa, cc))
start, end = map(int, input().split())

visited_se, first_answer = dijkstra(start, end, False)
visited_es, _ = dijkstra(end, start, False)

banned = None
route = [start]
dfs(start, 0)
banned = banned[1:-1]

print(first_answer + dijkstra(end, start, True)[1])
