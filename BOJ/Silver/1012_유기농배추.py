# 20240730
# 06:58

import sys
sys.setrecursionlimit(5000)


def dfs(y, x):
    visited[y][x] = 1
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and field[ny][nx] == 1:
            dfs(ny, nx)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        b, a = map(int, input().split())
        field[a][b] = 1

    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)


# 위는 재귀 활용, 아래는 스택 활용
"""
def dfs():
    cnt = 0

    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                now = i, j
                visited[i][j] = 1
                stk = []

                while True:
                    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ni, nj = now[0] + di, now[1] + dj
                        if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            stk.append(now)
                            now = ni, nj
                            break
                    else:
                        if stk:
                            now = stk.pop()
                        else:
                            break
    return cnt


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        b, a = map(int, input().split())
        field[a][b] = 1

    print(dfs())
"""