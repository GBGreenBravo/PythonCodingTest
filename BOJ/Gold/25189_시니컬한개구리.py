# 20241203
# 13:20
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs():
    visited0 = [[0] * M for _ in range(N)]
    visited0[sy][sx] = 1
    visited1 = [[0] * M for _ in range(N)]
    visited1[sy][sx] = 1
    row_used = [0] * N
    col_used = [0] * M
    queue = deque()
    queue.append((sy, sx, False))
    while queue:
        y, x, jumped = queue.popleft()
        distance = visited1[y][x] if jumped else visited0[y][x]

        if (y, x) == (ey, ex):
            print(distance - 1)
            return

        length = area[y][x]
        for dy, dx in direction:
            ny, nx = y + dy * length, x + dx * length
            if oob(ny, nx):
                continue
            if jumped:
                if visited1[ny][nx]:
                    continue
                visited1[ny][nx] = distance + 1
                queue.append((ny, nx, True))
            if not jumped:
                if visited0[ny][nx]:
                    continue
                visited0[ny][nx] = distance + 1
                queue.append((ny, nx, False))

        if jumped:
            continue

        if not row_used[y]:
            row_used[y] = 1
            for c in range(M):
                if not visited1[y][c]:
                    visited1[y][c] = distance + 1
                    queue.append((y, c, True))

        if not col_used[x]:
            col_used[x] = 1
            for r in range(N):
                if not visited0[r][x]:
                    visited1[r][x] = distance + 1
                    queue.append((r, x, True))

    print(-1)


N, M = map(int, input().split())
sy, sx, ey, ex = map(lambda inp: int(inp) - 1, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

bfs()
