# 20241126
# 55:54
# 1 / 3

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or 199 <= y or x < 0 or 199 <= x


def make_obstacle(y1, x1, y2, x2, y3, x3, y4, x4):
    if y2 < y4 and x2 < x4:
        for row in range(y1 + 1, y4):
            for col in range(x2 + 1, x1):
                area[row][col] = 1
        for row in range(y4, y3):
            for col in range(x2 + 1, x4):
                area[row][col] = 1
    elif y2 < y4 and x2 > x4:
        for row in range(y2 + 1, y4):
            for col in range(x3 + 1, x2):
                area[row][col] = 1
        for row in range(y4, y1):
            for col in range(x4 + 1, x1):
                area[row][col] = 1
    elif y2 > y4 and x2 > x4:
        for row in range(y3 + 1, y4 + 1):
            for col in range(x4 + 1, x3):
                area[row][col] = 1
        for row in range(y4 + 1, y2):
            for col in range(x1 + 1, x2):
                area[row][col] = 1
    else:  # elif y2 > y4 and x2 < x4:
        for row in range(y1 + 1, y4 + 1):
            for col in range(x1 + 1, x4):
                area[row][col] = 1
        for row in range(y4 + 1, y2):
            for col in range(x2 + 1, x3):
                area[row][col] = 1


si, sj = map(lambda inp: int(inp) - 1, input().split())
si, sj = si * 2, sj * 2
ei, ej = map(lambda inp: int(inp) - 1, input().split())
ei, ej = ei * 2, ej * 2
area = [[0] * 199 for _ in range(199)]
D = int(input())
for _ in range(D):
    py1, px1, py2, px2, py3, px3, py4, px4 = map(lambda inp: int(inp) - 1, input().split())
    py1, px1, py2, px2, py3, px3, py4, px4 = py1 * 2, px1 * 2, py2 * 2, px2 * 2, py3 * 2, px3 * 2, py4 * 2, px4 * 2
    make_obstacle(py1, px1, py2, px2, py3, px3, py4, px4)


def bfs():
    visited = [[0] * 199 for _ in range(199)]
    visited[si][sj] = 1

    queue = deque()
    for d_idx, (dy, dx) in enumerate(direction):
        ny, nx = si + dy, sj + dx
        if oob(ny, nx) or area[ny][nx]:
            continue
        nny, nnx = ny + dy, nx + dx
        visited[nny][nnx] = 1
        queue.append((0, nny, nnx, d_idx))

    while queue:
        turned_cnt, y, x, before_d_idx = queue.popleft()

        if turned_cnt + 1 > visited[y][x]:
            continue

        if y == ei and x == ej:
            print(turned_cnt)
            return

        dy, dx = direction[before_d_idx]
        ny, nx = y + dy, x + dx
        nny, nnx = ny + dy, nx + dx
        if not (oob(ny, nx) or area[ny][nx] or (0 < visited[nny][nnx] < turned_cnt + 1)):
            visited[nny][nnx] = turned_cnt + 1
            queue.appendleft((turned_cnt, nny, nnx, before_d_idx))

        dy, dx = direction[(before_d_idx + 1) % 4]
        ny, nx = y + dy, x + dx
        nny, nnx = ny + dy, nx + dx
        if not (oob(ny, nx) or area[ny][nx] or (0 < visited[nny][nnx] < turned_cnt + 2)):
            visited[nny][nnx] = turned_cnt + 2
            queue.append((turned_cnt + 1, nny, nnx, (before_d_idx + 1) % 4))

        dy, dx = direction[(before_d_idx - 1) % 4]
        ny, nx = y + dy, x + dx
        nny, nnx = ny + dy, nx + dx
        if not (oob(ny, nx) or area[ny][nx] or (0 < visited[nny][nnx] < turned_cnt + 2)):
            visited[nny][nnx] = turned_cnt + 2
            queue.append((turned_cnt + 1, nny, nnx, (before_d_idx - 1) % 4))


bfs()
