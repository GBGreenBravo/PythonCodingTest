# 20241008
# 09:33
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def bfs(sy, sx):
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or not area[ny][nx]:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))

    max_distance = max(map(max, visited))
    if max_distance == 1:
        return
    candidates = []
    for y in range(n):
        for x in range(m):
            if visited[y][x] == max_distance:
                candidates.append(area[sy][sx] + area[y][x])

    now_max = (max_distance - 1, max(candidates))
    global max_answer
    max_answer = max(max_answer, now_max)


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

max_answer = 0, 0
for i in range(n):
    for j in range(m):
        if area[i][j]:
            bfs(i, j)
print(max_answer[1])
