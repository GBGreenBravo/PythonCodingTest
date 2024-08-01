# 20240801
# 09:48
# 1 / 1

import sys
sys.setrecursionlimit(10000)


n = int(input())
picture = [list(str(input())) for _ in range(n)]

RGB = {'R': 1, "G": 2, "B": 3}
RG = {'R': 1, "G": 1, "B": 3}

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < n)


def dfs_RGB(y, x):
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if RGB[picture[ny][nx]] == RGB[picture[y][x]] and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs_RGB(ny, nx)


def dfs_RG(y, x):
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if RG[picture[ny][nx]] == RG[picture[y][x]] and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs_RG(ny, nx)


visited = [[0] * n for _ in range(n)]
cnt_RGB = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs_RGB(i, j)
            cnt_RGB += 1


visited = [[0] * n for _ in range(n)]
cnt_RG = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs_RG(i, j)
            cnt_RG += 1

print(cnt_RGB, cnt_RG)


# 아래는 BFS로 푼 코드
"""
from collections import deque

n = int(input())
picture = [list(str(input())) for _ in range(n)]

RGB = {'R': 1, "G": 2, "B": 3}
RG = {'R': 1, "G": 1, "B": 3}

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < n)


def bfs_RGB(sy, sx, RG_same):
    visited[sy][sx] = 1
    queue = deque([(sy, sx)])
    RGB_decoder = RG if RG_same else RGB

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if RGB_decoder[picture[ny][nx]] == RGB_decoder[picture[y][x]] and not visited[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx))


visited = [[0] * n for _ in range(n)]
cnt_RGB = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_RGB(i, j, False)
            cnt_RGB += 1


visited = [[0] * n for _ in range(n)]
cnt_RG = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_RGB(i, j, True)
            cnt_RG += 1

print(cnt_RGB, cnt_RG)
"""