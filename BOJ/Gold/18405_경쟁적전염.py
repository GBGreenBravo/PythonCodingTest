# 20240929
# 08:32
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
second, ey, ex = map(int, input().split())

viruses = [None] + [[] for _ in range(k)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if area[i][j]:
            visited[i][j] = area[i][j]
            viruses[area[i][j]].append((i, j))

queue = []
for i in range(1, k + 1):
    queue.extend(viruses[i])

for _ in range(1, second + 1):
    next_queue = []
    for y, x in queue:
        now_virus = visited[y][x]
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx]:
                continue
            visited[ny][nx] = now_virus
            next_queue.append((ny, nx))
    queue = next_queue

print(visited[ey - 1][ex - 1] if visited[ey - 1][ex - 1] else 0)
