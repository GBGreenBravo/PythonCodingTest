# 20240725
# 07:32

from copy import deepcopy


def bfs(y, x):
    visited[y][x] = 0
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 1:
            bfs(ny, nx)


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    mp = [list(map(int, input().split())) for _ in range(h)]

    visited = deepcopy(mp)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)


# 큐 활용한다면 아래와 같이. (메모리/시간 둘다 감축됨)
"""
from collections import deque
from copy import deepcopy


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 0
    while queue:
        a, b = queue.popleft()
        for da, db in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            na, nb = a + da, b + db
            if 0 <= na < h and 0 <= nb < w and visited[na][nb] == 1:
                visited[na][nb] = 0
                queue.append((na, nb))


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    mp = [list(map(int, input().split())) for _ in range(h)]

    visited = deepcopy(mp)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)
"""