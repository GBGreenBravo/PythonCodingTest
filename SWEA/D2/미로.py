# 20240730
# 13:08

def dfs(start):
    visited = [[0] * n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    for a in range(n):
        for b in range(n):
            if maze[a][b] == 1:
                visited[a][b] = 1

    stk = []

    y, x = start[0], start[1]
    while True:
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                stk.append((y, x))
                y, x = ny, nx
                break
        else:
            if stk:
                y, x = stk.pop()
            else:
                break

    return visited[end_point[0]][end_point[1]]


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [[int(i) for i in list(str(input()))] for _ in range(n)]

    start_point, end_point = None, None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_point = (i, j)
                break
            elif maze[i][j] == 3:
                end_point = (i, j)

    print(f"#{test_case} {dfs(start_point)}")


# 위는 스택 활용, 아래는 재귀 활용
# 그리고 아래에서는 connected에 갈 수 있는 경로를 먼저 넣어줬음.
"""
def dfs(node):
    y, x = node
    visited[y][x] = 1
    for ny, nx in connected[y][x]:
        if visited[ny][nx] == 0:
            dfs((ny, nx))


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maze = [[int(i) for i in list(str(input()))] for _ in range(n)]

    connected = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] != 1:
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1:
                        connected[i][j].append((ni, nj))


    start_point, end_point = None, None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_point = (i, j)
            elif maze[i][j] == 3:
                end_point = (i, j)

    visited = [[0] * n for _ in range(n)]
    dfs(start_point)

    print(f"#{test_case} {visited[end_point[0]][end_point[1]]}")
"""