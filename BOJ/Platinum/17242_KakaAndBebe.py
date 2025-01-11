# 20250111
# 26:00
# 1 / 2

from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra():
    visited = [[1001 for _ in range(1001)] for _ in range(N)]
    visited[0][0] = 0
    min_visited = [[(1001, 1001) for _ in range(3)] for _ in range(N)]
    min_visited[0][1] = (0, 0)

    queue = [(0, 0, 0, 0)]
    while queue:
        stress, now, kaka, bebe = heappop(queue)

        if visited[now][kaka] != bebe:
            continue

        if now == N - 1:
            print(stress)
            return

        for nex, added_kaka, added_bebe in connected[now]:
            next_kaka, next_bebe = kaka + added_kaka, bebe + added_bebe
            if 1000 < next_kaka or 1000 < next_bebe:
                continue
            if visited[nex][next_kaka] <= next_bebe:
                continue

            if next_kaka < next_bebe:
                if min_visited[nex][0][0] <= next_kaka and min_visited[nex][0][1] <= next_bebe:
                    continue
                min_visited[nex][0] = min(min_visited[nex][0], (next_kaka, next_bebe))
            elif next_kaka == next_bebe:
                if min_visited[nex][1][0] <= next_kaka:
                    continue
                min_visited[nex][1] = min(min_visited[nex][1], (next_kaka, next_bebe))
            else:
                if min_visited[nex][2][0] <= next_kaka and min_visited[nex][2][1] <= next_bebe:
                    continue
                min_visited[nex][2] = min(min_visited[nex][2], (next_kaka, next_bebe), key=lambda mv: mv[1])

            visited[nex][next_kaka] = next_bebe
            heappush(queue, (next_kaka * next_bebe, nex, next_kaka, next_bebe))

    answer = 1001 ** 2
    for kaka, bebe in enumerate(visited[-1]):
        if not kaka or bebe == 1001:
            continue
        answer = min(answer, kaka * bebe)
    print(answer if answer != 1001 ** 2 else -1)


N, M = map(int, input().split())
connected = [[] for _ in range(N)]
for _ in range(M):
    aa, bb, cc, dd = map(int, input().split())
    connected[aa].append((bb, cc, dd))
    connected[bb].append((aa, cc, dd))
dijkstra()
