# 20240920
# 12:26
# 1 / 1

from collections import deque

direction = ((0, -1), (-1, 0), (0, 1), (1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


m, n = map(int, input().split())
connected = [list(map(int, input().split())) for _ in range(n)]
area = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
group_cnts = [0]
group_flag = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            queue = deque()
            queue.append((i, j))

            group_flag += 1
            area[i][j] = group_flag
            group_cnt = 1

            while queue:
                y, x = queue.popleft()
                for d in range(4):
                    if connected[y][x] >> d & 1:
                        continue
                    dy, dx = direction[d]
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx]:
                        continue
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    area[ny][nx] = group_flag
                    group_cnt += 1

            group_cnts.append(group_cnt)

print(group_flag)
print(max(group_cnts))

mx_answer = 0
for i in range(n):
    for j in range(m):
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if oob(ni, nj) or area[ni][nj] == area[i][j]:
                continue
            mx_answer = max(mx_answer, group_cnts[area[i][j]] + group_cnts[area[ni][nj]])
print(mx_answer)
