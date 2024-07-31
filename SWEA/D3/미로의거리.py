# 20240731
# 10:28

def bfs(start_node):
    visited = [[0] * n for _ in range(n)]
    visited[start_node[0]][start_node[1]] = 1
    queue = [(start_node[0], start_node[1], 0)]

    while queue:
        y, x, distance = queue.pop(0)
        distance += 1
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx

            if not(0 <= ny < n) or not(0 <= nx < n):
                continue

            if visited[ny][nx] == 0 and (maze[ny][nx] == 0 or maze[ny][nx] == 3):
                visited[ny][nx] = distance
                queue.append((ny, nx, distance))
            elif visited[ny][nx] > distance and (maze[ny][nx] == 0 or maze[ny][nx] == 3):
                visited[ny][nx] = distance
                queue.append((ny, nx, distance))

    return visited[end[0]][end[1]] - 1 if visited[end[0]][end[1]] != 0 else 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [[int(i) for i in list(str(input()))] for _ in range(n)]

    start, end = None, None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = i, j
            elif maze[i][j] == 3:
                end = i, j

    print(f"#{test_case} {bfs(start)}")
