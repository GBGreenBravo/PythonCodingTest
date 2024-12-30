# 20241230
# 26:45
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs(height, sy, sx):
    global answer

    criteria = height - D
    possible = True
    now_answer = 1

    visited[sy][sx] = height
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if area[ny][nx] <= criteria:
                continue
            if visited[ny][nx] != -1:
                if visited[ny][nx] != height:
                    possible = False
                continue
            if area[ny][nx] == height:
                now_answer += 1
            visited[ny][nx] = height
            queue.append((ny, nx))

    if possible:
        answer += now_answer


T = int(input())
for _ in range(T):
    N, M, D = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    indexes = []
    for i in range(N):
        for j in range(M):
            indexes.append((area[i][j], i, j))
    indexes.sort(reverse=True)

    answer = 0
    visited = [[-1] * M for _ in range(N)]
    for h, i, j in indexes:
        if visited[i][j] != -1:
            continue
        bfs(h, i, j)

    print(answer)
