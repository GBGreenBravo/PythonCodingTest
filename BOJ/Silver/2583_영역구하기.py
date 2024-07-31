# 20240730
# 13:46

import sys
sys.setrecursionlimit(10000)


def dfs(y, x):
    visited[y][x] = 1
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and paper[ny][nx] == 0 and visited[ny][nx] == 0:
            dfs(ny, nx)


m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

cnt = 0
areas = []
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and paper[i][j] == 0:
            cnt += 1
            before = sum([sum(row) for row in visited])
            dfs(i, j)
            after = sum([sum(row) for row in visited])
            areas.append(after - before)

print(cnt)
print(*sorted(areas))


# 아래는 area를 dfs() 내에서 구해서 반납한 코드
"""
import sys
sys.setrecursionlimit(10000)


def dfs(y, x):
    area = 1
    visited[y][x] = 1
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and paper[ny][nx] == 0 and visited[ny][nx] == 0:
            area += dfs(ny, nx)
    return area


m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

cnt = 0
areas = []
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and paper[i][j] == 0:
            cnt += 1
            areas.append(dfs(i, j))

print(cnt)
print(*sorted(areas))
"""


# 위 두 답변은 재귀 활용, 아래는 스택 활용
"""
def dfs():
    visited = [[0] * n for _ in range(m)]
    areas = []

    for y in range(m):
        for x in range(n):
            if paper[y][x] == 0 and visited[y][x] == 0:
                now = y, x
                visited[y][x] = 1
                stk = []

                area = 1
                while True:
                    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ny, nx = now[0] + dy, now[1] + dx
                        if 0 <= ny < m and 0 <= nx < n and paper[ny][nx] == 0 and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            stk.append(now)
                            now = ny, nx
                            area += 1
                            break
                    else:
                        if stk:
                            now = stk.pop()
                        else:
                            break

                areas.append(area)

    return areas


m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

answers = dfs()
print(len(answers))
print(*sorted(answers))
"""