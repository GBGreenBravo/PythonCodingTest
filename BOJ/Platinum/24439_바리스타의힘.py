# 20241204
# 48:09
# 1 / 3

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def get_visited_start(sy, sx):
    visited = [[1e6] * M for _ in range(N)]
    visited[sy][sx] = 0
    queue = deque()
    queue.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] != 1e6 or area[ny][nx]:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny,nx))
    return visited


def get_visited_end(sy, sx):
    visited = [[1e6] * M for _ in range(N)]
    visited[sy][sx] = 0
    queue = deque()
    queue.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] != 1e6:
                continue
            if area[ny][nx]:
                visited[ny][nx] = distance + 1
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny,nx))
    return visited


def barista_power():
    global answer

    for y in range(N):
        for x in range(M):
            if from_start[y][x] != 1e6:
                for d_idx, (dy, dx) in enumerate(direction):
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or not area[ny][nx]:
                        continue

                    now_d = from_start[y][x]

                    my, mx = ny, nx
                    d = 1
                    while not oob(my, mx):
                        answer = min(answer, now_d + d + from_end[my][mx])
                        d += 1
                        my, mx = my + dy, mx + dx


N, M = map(int, input().split())
area = [[int(i) for i in str(input())] for _ in range(N)]

from_start = get_visited_start(0, 0)
from_end = get_visited_end(N - 1, M - 1)

answer = from_start[-1][-1]
barista_power()
print(-1 if answer == 1e6 else answer)
