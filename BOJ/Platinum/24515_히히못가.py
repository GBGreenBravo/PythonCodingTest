# 20241230
# 19:35
# 1 / 1

from collections import deque
from heapq import heappush, heappop

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def dijkstra():
    visited = [[N**2] * N for _ in range(N)]
    pq = []
    for c in range(1, N - 1):
        visited[0][c] = group_cnt[0][c]
        heappush(pq, (group_cnt[0][c], 0, c))
    for r in range(N - 1):
        visited[r][N - 1] = group_cnt[r][N - 1]
        heappush(pq, (group_cnt[r][N - 1], r, N - 1))

    while pq:
        cost, y, x = heappop(pq)

        if visited[y][x] != cost:
            continue

        if (y != 0 and x == 0) or (x != N - 1 and y == N - 1):
            print(cost)
            return

        for d_idx, (dy, dx) in enumerate(direction_8):
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            next_cost = cost
            if d_idx >= 4 or area[ny][nx] != area[y][x]:
                next_cost += group_cnt[ny][nx]
            if next_cost < visited[ny][nx]:
                visited[ny][nx] = next_cost
                heappush(pq, (next_cost, ny, nx))


N = int(input())
area = [list(str(input())) for _ in range(N)]
group_cnt = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not group_cnt[i][j]:
            group_cnt[i][j] = -1
            group_arr = [(i, j)]
            dq = deque([(i, j)])
            while dq:
                ci, cj = dq.popleft()
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if oob(ni, nj) or group_cnt[ni][nj] == -1 or area[ci][cj] != area[ni][nj]:
                        continue
                    group_cnt[ni][nj] = -1
                    dq.append((ni, nj))
                    group_arr.append((ni, nj))
            for gi, gj in group_arr:
                group_cnt[gi][gj] = len(group_arr)

dijkstra()
