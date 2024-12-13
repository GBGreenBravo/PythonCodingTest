# 20241213
# 27:06
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def bfs():
    global min_answer

    ey, ex = N - 1, N - 1
    visited = [[[201] * 201 for _ in range(N)] for _ in range(N)]
    visited[0][0][area[0][0]] = area[0][0]
    queue = deque()
    queue.append((0, 0, area[0][0], area[0][0]))
    while queue:
        y, x, now_min, now_max = queue.popleft()
        if now_max - now_min >= min_answer:
            continue
        if y == ey and x == ex:
            min_answer = min(min_answer, now_max - now_min)
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            next_min, next_max = min(now_min, area[ny][nx]), max(now_max, area[ny][nx])
            if visited[ny][nx][next_min] <= next_max:
                continue
            visited[ny][nx][next_min] = next_max
            queue.append((ny, nx, next_min, next_max))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
min_answer = 201
bfs()
print(min_answer)
