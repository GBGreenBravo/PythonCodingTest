# 20241214
# 1:11:54
# 1 / 9

from heapq import heappop, heappush
from collections import deque
import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    S, D = map(int, input().split())
    connected = [[] for _ in range(N)]
    for _ in range(M):
        aa, bb, cc = map(int, input().split())
        connected[aa].append((bb, cc))

    shortest = None
    banned = set()
    min_befores = [[] for _ in range(N)]
    distances = [1e7] * N
    distances[S] = 0
    queue = []
    heappush(queue, (0, S))
    while queue:
        distance, now = heappop(queue)
        if distance != distances[now]:
            continue
        if shortest and shortest < distance:
            break
        if now == D:
            shortest = distance
            q = deque([D])
            v = [0] * N
            v[D] = 1
            while q:
                n = q.popleft()
                for nn in min_befores[n]:
                    banned.add((nn, n))
                    if not v[nn]:
                        v[nn] = 1
                        q.append(nn)
            continue
        for nex, added in connected[now]:
            if distances[nex] > distance + added:
                distances[nex] = distance + added
                heappush(queue, (distance + added, nex))
                min_befores[nex] = [now]
            elif distances[nex] == distance + added:
                min_befores[nex].append(now)

    second_shortest = None
    distances = [1e7] * N
    distances[S] = 0
    queue = []
    heappush(queue, (0, S))
    while queue:
        distance, now = heappop(queue)
        if distance != distances[now]:
            continue
        if now == D:
            second_shortest = distance
            break
        for nex, added in connected[now]:
            if distances[nex] > distance + added and (now, nex) not in banned:
                distances[nex] = distance + added
                heappush(queue, (distance + added, nex))

    print(second_shortest if second_shortest else -1)
