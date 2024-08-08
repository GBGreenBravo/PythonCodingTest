# 20240808
# 40:22
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (n <= x)


def bfs_find_zero(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True

    mine_zero_found = False

    while queue:
        y, x = queue.popleft()
        mine = 0
        next = []
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if area[ny][nx] == '*':
                mine += 1
                continue
            if not visited[ny][nx]:
                next.append((ny, nx))

        if mine == 0:
            mine_zero_found = True
            for ny, nx in next:
                visited[ny][nx] = True
            queue.extend(next)

    if not mine_zero_found:
        visited[sy][sx] = False

    return True if mine_zero_found else False


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    area = [list(str(input())) for _ in range(n)]

    answer_click_cnt = 0

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] == '.' and not visited[i][j]:
                if bfs_find_zero(i, j):
                    answer_click_cnt += 1

    for i in range(n):
        for j in range(n):
            if area[i][j] == '.' and not visited[i][j]:
                answer_click_cnt += 1

    print(f"#{test} {answer_click_cnt}")
