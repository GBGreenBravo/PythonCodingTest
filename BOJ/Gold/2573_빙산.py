# 20240729
# 17:38

from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < m)


def melt():
    global area
    melting_area = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if area[i][j] != 0:
                degree = 0
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if oob(ni, nj):
                        continue
                    if area[ni][nj] == 0:
                        degree += 1
                melting_area[i][j] = max(0, area[i][j] - degree)

    area = melting_area


def bfs(a, b):
    queue = deque()
    gone[a][b] = 0
    queue.append((a, b))
    while queue:
        y, x = queue.pop()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if gone[ny][nx] != 0:
                gone[ny][nx] = 0
                queue.append((ny, nx))


day = 0
while True:
    gone = deepcopy(area)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if gone[i][j] != 0:
                cnt += 1
                bfs(i, j)
    if cnt == 1:
        day += 1
        melt()
        continue
    elif cnt > 1:
        print(day)
        break
    elif cnt == 0:
        print(0)
        break


# deepcopy 이용하면 시간 꽤 많이 쓰임.
# 다른 방법이 있다면 아래와 같이 deepcopy 쓰지 말자.
"""
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < m)


def melt():
    melting = []

    for i in range(n):
        for j in range(m):
            if area[i][j] != 0:
                degree = 0
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if oob(ni, nj):
                        continue
                    if area[ni][nj] == 0:
                        degree += 1
                melting.append((i, j, max(0, area[i][j] - degree)))

    for y, x, height in melting:
        area[y][x] = height


def bfs(a, b):
    queue = deque()
    gone[a][b] = True
    queue.append((a, b))
    while queue:
        y, x = queue.pop()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if area[ny][nx] != 0 and not gone[ny][nx]:
                gone[ny][nx] = True
                queue.append((ny, nx))


day = 0
while True:
    gone = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] != 0 and not gone[i][j]:
                if cnt > 1:
                    break
                cnt += 1
                bfs(i, j)
        else:
            continue
        break
    if cnt == 1:
        day += 1
        melt()
        continue
    elif cnt == 2:
        print(day)
        break
    elif cnt == 0:
        print(0)
        break
"""