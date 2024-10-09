# 20241009
# 21:00
# 1 / 2

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def dfs(cnt, y, x):
    global max_answer
    max_answer = max(max_answer, cnt)

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or visited[ny][nx] or area[ny][nx] >= area[y][x]:
            continue
        visited[ny][nx] = 1
        dfs(cnt + 1, ny, nx)
        visited[ny][nx] = 0


t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_answer = 1

    start_value = max(map(max, area))
    for ii in range(n):
        for jj in range(n):
            if area[ii][jj] == start_value:
                visited = [[0] * n for _ in range(n)]
                visited[ii][jj] = 1
                dfs(1, ii, jj)

    for i in range(n):
        for j in range(n):
            for _ in range(k):
                area[i][j] -= 1

                for ii in range(n):
                    for jj in range(n):
                        if area[ii][jj] == start_value:
                            visited = [[0] * n for _ in range(n)]
                            visited[ii][jj] = 1
                            dfs(1, ii, jj)

            area[i][j] += k

    print(f"#{test} {max_answer}")


# 아래는 BFS 풀이; 더 효율적임
"""
from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def bfs(sy, sx):
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] >= area[y][x] or visited[ny][nx] >= distance + 1:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))

    global max_answer
    max_answer = max(max_answer, max(map(max, visited)))


t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_answer = 1

    start_value = max(map(max, area))
    for ii in range(n):
        for jj in range(n):
            if area[ii][jj] == start_value:
                bfs(ii, jj)

    for i in range(n):
        for j in range(n):
            for _ in range(k):
                area[i][j] -= 1

                for ii in range(n):
                    for jj in range(n):
                        if area[ii][jj] == start_value:
                            bfs(ii, jj)

            area[i][j] += k

    print(f"#{test} {max_answer}")
"""