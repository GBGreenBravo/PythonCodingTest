# 20240812
# 25:33
# 1 / 1

import sys
sys.setrecursionlimit(10_000)

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (n <= x)


def dfs(y, x):
    near = []  # 주변에 더 작은 값이 있다면, 담을 배열
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or forest[ny][nx] >= forest[y][x]:  # 범위 밖이거나, 크거나 같은 값이면 continue
            continue
        if visited[ny][nx]:  # 이전에 방문했던 곳이면
            near.append(visited[ny][nx])  # 그 값을 그대로 near에 저장. (그 좌표에서는 이미 작은 곳 다 탐색했으므로)
        if not visited[ny][nx]:  # 방문하지 않은 곳이라면
            visited[ny][nx] = dfs(ny, nx)  # 재귀를 통해 그 좌표에서의 값을 먼저 저장
            near.append(visited[ny][nx])  # 위의 재귀에서 반환한 값 그대로 near에 저장
    return max(near) + 1 if near else 1  # 주변에 더 작은 값이 없다면 1, 있다면 그 최대값 + 1


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:  # visited 돼있는 좌표는 또 살펴볼 필요 없음.
            visited[i][j] = dfs(i, j)

print(max(map(max, visited)))
