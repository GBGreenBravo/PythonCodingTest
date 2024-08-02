# 20240802
# 13:53
# 1 / 1

from collections import deque

direction = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

visited = [[[0] * m for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                visited[i][j][k] = 1
                queue.append((i, j, k))
            elif tomatoes[i][j][k] == -1:
                visited[i][j][k] = -1


def oob(hh, yy, xx):
    return not(0 <= hh < h) or not(0 <= yy < n) or not(0 <= xx < m)


while queue:
    ch, cy, cx = queue.popleft()
    days = visited[ch][cy][cx] + 1

    for dh, dy, dx in direction:
        nh, ny, nx = ch + dh, cy + dy, cx + dx
        if oob(nh, ny, nx) or tomatoes[nh][ny][nx] == -1 or visited[nh][ny][nx] > 0:
            continue
        visited[nh][ny][nx] = days
        queue.append((nh, ny, nx))

answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            day = visited[i][j][k]
            if day > answer:
                answer = day
            elif day == 0:
                answer = 0
                break
        else:
            continue
        break
    else:
        continue
    break

print(answer - 1)
