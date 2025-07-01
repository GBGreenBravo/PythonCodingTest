"""
20241214 풀이:
    노드별로 최단거리로 가는 이전노드를 기록하는 걸,
    도착점까지 다 계산한 후에,
    도착점에서 역으로 BFS하면서 banned에 가면 안되는 도로 기록.
    이 banned 정보를 기반으로 dijkstra했음.
20250701 풀이:
    시작점에서 각 노드까지의 최단거리, 도착점에서 각 노드까지의 최단거리
    를 각각 계산해놓고,
    (시작점에 현재노드 최단거리 + 현재노드-다음노드 거리 + 도착점에서 다음노드 최단거리)가
    (최단경로 길이)와 같으면 안된다는 걸 조건으로 dijkstra했음.
"""


# 20250701
# 32:16
# 1 / 2

from heapq import heappush, heappop


def calulate_shortest_from_start():
    dist = [10**8 for _ in range(N)]

    dist[S] = 0
    queue = [(0, S)]
    while queue:
        dis, now = heappop(queue)
        if dis > dist[E]:
            break
        if dist[now] != dis:
            continue
        for nex, added in connected[now]:
            if dis + added >= dist[nex]:
                continue
            dist[nex] = dis + added
            heappush(queue, (dis + added, nex))

    return dist


def calulate_shortest_from_end():
    dist = [10**8 for _ in range(N)]

    dist[E] = 0
    queue = [(0, E)]
    while queue:
        dis, now = heappop(queue)
        if dis > dist[S]:
            break
        if dist[now] != dis:
            continue
        for nex, added in connected_reverse[now]:
            if dis + added >= dist[nex]:
                continue
            dist[nex] = dis + added
            heappush(queue, (dis + added, nex))

    return dist


while True:
    N, M = map(int, input().split())
    if N + M == 0:
        break

    connected = [list() for _ in range(N)]
    connected_reverse = [list() for _ in range(N)]

    S, E = map(int, input().split())
    for _ in range(M):
        u, v, p = map(int, input().split())
        connected[u].append((v, p))
        connected_reverse[v].append((u, p))

    shortest_from_start = calulate_shortest_from_start()
    shortest_from_end = calulate_shortest_from_end()

    shortest_dist = shortest_from_start[E]

    almost_dist = [10**8 for _ in range(N)]
    almost_dist[S] = 0
    queue = [(0, S)]
    while queue:
        dis, now = heappop(queue)
        if almost_dist[now] != dis:
            continue
        if now == E:
            break
        for nex, added in connected[now]:
            if shortest_from_start[now] + added + shortest_from_end[nex] == shortest_dist:
                continue
            if almost_dist[nex] <= dis + added:
                continue
            almost_dist[nex] = dis + added
            heappush(queue, (dis + added, nex))

    print(-1 if almost_dist[E] == 10**8 else almost_dist[E])


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
