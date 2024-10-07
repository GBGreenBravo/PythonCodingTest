# 20241007
# 12:12
# 1 / 1

from collections import deque


direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yyy, xxx):
    return yyy < 0 or n <= yyy or xxx < 0 or m <= xxx


n, m, a, b, k = map(int, input().split())
area = [[0] * m for _ in range(n)]
for _ in range(k):
    aa, bb = map(lambda inp: int(inp) - 1, input().split())
    area[aa][bb] = 1
sy, sx = map(lambda inp: int(inp) - 1, input().split())
ey, ex = map(lambda inp: int(inp) - 1, input().split())

visited = [[0] * m for _ in range(n)]
visited[sy][sx] = 1

queue = deque()
queue.append((sy, sx))

while queue:
    y, x = queue.popleft()
    for dy, dx in direction:
        ny, nx = y + dy, x + dx

        if oob(ny, nx) or visited[ny][nx]:
            continue

        for yy in range(ny, ny + a):
            for xx in range(nx, nx + b):
                if oob(yy, xx) or area[yy][xx]:
                    break
            else:
                continue
            break
        else:
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))

print(visited[ey][ex] - 1)
