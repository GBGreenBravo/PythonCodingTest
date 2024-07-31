# 202040731
# 06:34

n, m = map(int, input().split())
maze = [[int(i) for i in list(str(input()))] for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
queue = [(0, 0)]


def oob(yy, xx):
    return not(0 <= yy < n) or not(0 <= xx < m)


direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
while queue:
    y, x = queue.pop(0)
    distance = visited[y][x] + 1

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if maze[ny][nx] != 1:
            continue
        if visited[ny][nx] == 0 or visited[ny][nx] > distance:  # BFS이므로, 뒤의 조건은 필요 없음.
            visited[ny][nx] = distance
            queue.append((ny, nx))

print(visited[n - 1][m - 1])
