# 20241006
# 28:12
# 1 / 1

from collections import deque

direction = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))


def oob(z, y, x):
    return z < 0 or 5 <= z or y < 0 or 5 <= y or x < 0 or 5 <= x


def bfs(arr):
    if not arr[0][0][0] or not arr[4][4][4]:
        return

    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1

    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in direction:
            nz, ny, nx = z + dz, y + dy, x + dx
            if oob(nz, ny, nx) or visited[nz][ny][nx] or not arr[nz][ny][nx]:
                continue
            visited[nz][ny][nx] = visited[z][y][x] + 1
            queue.append((nz, ny, nx))

    global min_answer
    if visited[4][4][4]:
        min_answer = min(min_answer, visited[4][4][4] - 1)


def dfs_4(arr):
    if min_answer == 12:
        return
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        area = [boards[a][arr[0]], boards[b][arr[1]], boards[c][arr[2]], boards[d][arr[3]], boards[e][arr[4]]]
                        bfs(area)


def dfs_5(cnt, five_arr):
    if min_answer == 12:
        return
    if cnt == 5:
        dfs_4(five_arr)
        return

    for idx in range(5):
        if idx not in five_arr:
            dfs_5(cnt + 1, five_arr + [idx])


boards = [[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]] + [[] for _ in range(3)]
for i in range(5):
    now_board = boards[0][i]
    for j in range(1, 4):
        now_board = [list(row)[::-1] for row in zip(*now_board)]
        boards[j].append(now_board)

min_answer = 5**3
dfs_5(0, [])
print(-1 if min_answer == 5**3 else min_answer)
