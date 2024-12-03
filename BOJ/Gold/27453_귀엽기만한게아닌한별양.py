# 20241203
# 1:08:00
# 1 / 10

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs():
    visited = [[[] for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((sy, sx, (0, 0), 0, 0))
    while queue:
        y, x, before, before_ache, distance = queue.popleft()
        now_ache = area[y][x]
        if (y, x) == (ey, ex):
            print(distance)
            return

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == -1:
                continue

            if before == (ny, nx):
                continue

            if before_ache + now_ache + area[ny][nx] > K:
                continue

            if y * M + x in visited[ny][nx]:
                continue

            visited[ny][nx].append(y * M + x)
            queue.append((ny, nx, (y, x), now_ache, distance + 1))

    print(-1)


N, M, K = map(int, input().split())
area = [list(str(input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if area[i][j] == 'X':
            area[i][j] = -1
        elif area[i][j] == 'S':
            area[i][j] = 0
            sy, sx = i, j
        elif area[i][j] == 'H':
            area[i][j] = 0
            ey, ex = i, j
        else:
            area[i][j] = int(area[i][j])
bfs()
