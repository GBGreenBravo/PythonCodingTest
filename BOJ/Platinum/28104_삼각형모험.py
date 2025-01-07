# 20250107
# 40:38
# 1 / 3

import sys
from collections import deque

input = sys.stdin.readline
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def grouping(sy, sx):
    visited[sy][sx] = group_flag
    group_arr = deque([(sy, sx)])
    circular.append(0)

    queue = deque()
    for c_idx, (cy, cx) in enumerate(connected[sy][sx]):
        searching_direction = int(not c_idx)
        visited[cy][cx] = group_flag
        if searching_direction:
            group_arr.appendleft((cy, cx))
        else:
            group_arr.append((cy, cx))
        queue.append((cy, cx, sy, sx, searching_direction))

    while queue:
        y, x, by, bx, searching_direction = queue.popleft()
        for ny, nx in connected[y][x]:
            if ny == by and nx == bx:
                continue
            if visited[ny][nx]:
                circular[group_flag] = 1
                break
            visited[ny][nx] = group_flag
            if searching_direction:
                group_arr.appendleft((ny, nx))
            else:
                group_arr.append((ny, nx))
            queue.append((ny, nx, y, x, searching_direction))

    group_lengths.append(len(group_arr))
    for g_idx, (y, x) in enumerate(group_arr):
        group_indexes[y][x] = g_idx


N, M, Q = map(int, input().split())
t_area = [list(str(input())) for _ in range(N)]
queries = [tuple(map(lambda inp: int(inp) - 1, input().split())) for _ in range(Q)]

connected = [[[] for _ in range(M)] for _ in range(2 * N)]
for i in range(N):
    for j in range(M):
        up, down = i * 2, i * 2 + 1

        if i != 0:
            connected[up][j].append((up - 1, j))
        if i != N - 1:
            connected[down][j].append((down + 1, j))

        if t_area[i][j] == 'N':
            if j != 0:
                if t_area[i][j - 1] == 'N':
                    connected[down][j].append((up, j - 1))
                else:
                    connected[down][j].append((down, j - 1))
            if j != M - 1:
                if t_area[i][j + 1] == 'N':
                    connected[up][j].append((down, j + 1))
                else:
                    connected[up][j].append((up, j + 1))

        else:
            if j != 0:
                if t_area[i][j - 1] == 'N':
                    connected[up][j].append((up, j - 1))
                else:
                    connected[up][j].append((down, j - 1))
            if j != M - 1:
                if t_area[i][j + 1] == 'N':
                    connected[down][j].append((down, j + 1))
                else:
                    connected[down][j].append((up, j + 1))

group_flag = 0
group_lengths = [None]
circular = [None]
group_indexes = [[-1] * M for _ in range(2 * N)]
visited = [[0] * M for _ in range(2 * N)]
for i in range(2 * N):
    for j in range(M):
        if not visited[i][j]:
            group_flag += 1
            grouping(i, j)

for x1, y1, t1, x2, y2, t2 in queries:
    x1 *= 2
    if not t1:
        x1 += 1
    x2 *= 2
    if not t2:
        x2 += 1

    if visited[x1][y1] != visited[x2][y2]:
        print(-1)
    else:
        group_idx = visited[x1][y1]
        idx1 = group_indexes[x1][y1]
        idx2 = group_indexes[x2][y2]
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        if not circular[group_idx]:
            print(idx2 - idx1)
        else:
            print(min(idx2 - idx1, group_lengths[group_idx] - idx2 + idx1))
