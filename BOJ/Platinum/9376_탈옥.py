# 20241225
# 1 / 5

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or H + 2 <= y or x < 0 or W + 2 <= x


def bfs(sy, sx):
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[sy][sx] = 1
    queue = deque([(1, sy, sx)])
    while queue:
        flag, y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == '*':
                continue
            elif area[ny][nx] == '#':
                visited[ny][nx] = flag + 1
                queue.append((flag + 1, ny, nx))
            else:
                visited[ny][nx] = flag
                queue.appendleft((flag, ny, nx))
    return visited


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    area = [['.'] * (W + 2)] + [['.'] + list(str(input())) + ['.'] for _ in range(H)] + [['.'] * (W + 2)]

    first = False
    for i in range(H + 2):
        for j in range(W + 2):
            if area[i][j] == '$':
                area[i][j] = '.'
                if not first:
                    first = i, j
                else:
                    second = i, j

    start_visited = bfs(0, 0)
    first_visited = bfs(*first)
    second_visited = bfs(*second)

    answer = W * H
    for i in range(H + 2):
        for j in range(W + 2):
            if start_visited[i][j] and first_visited[i][j] and second_visited[i][j]:
                now = start_visited[i][j] + first_visited[i][j] + second_visited[i][j] - 3
                if area[i][j] == '#':
                    now -= 2
                answer = min(answer, now)
    print(answer)
