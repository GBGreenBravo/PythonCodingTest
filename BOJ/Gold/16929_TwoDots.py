# 20240915
# 19:02
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1

            queue = deque()
            queue.append((i, j, 1))

            while queue:
                y, x, distance = queue.popleft()
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or area[y][x] != area[ny][nx]:
                        continue
                    if visited[ny][nx]:
                        if visited[ny][nx] > distance:
                            print('Yes')
                            break
                        continue
                    visited[ny][nx] = distance + 1
                    queue.append((ny, nx, distance + 1))
                else:
                    continue
                break
            else:
                continue
            break
    else:
        continue
    break
else:
    print('No')


# 위는 BFS 풀이
# 아래는 DFS 풀이
"""
def dfs(y, x, distance):
    results = []
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if ny < 0 or n <= ny or nx < 0 or m <= nx or area[y][x] != area[ny][nx]:
            continue
        if visited[ny][nx]:
            if distance - visited[ny][nx] > 1:
                return True
            continue
        visited[ny][nx] = distance + 1
        results.append(dfs(ny, nx, distance + 1))
    return sum(results)


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            if dfs(i, j, 1):
                print('Yes')
                break
    else:
        continue
    break
else:
    print('No')
"""