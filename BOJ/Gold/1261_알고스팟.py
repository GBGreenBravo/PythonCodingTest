# 20240816
# 07:30
# 1 / 1

from heapq import heappush, heappop

m, n = map(int, input().split())
area = [[int(i) for i in list(str(input()))] for _ in range(n)]

INF = 1e4
visited = [[INF] * m for _ in range(n)]
visited[0][0] = 0
queue = [(0, 0, 0)]

while queue:
    distance, y, x = heappop(queue)

    if y == n - 1 and x == m - 1:
        print(distance)
        break

    if visited[y][x] < distance:
        continue

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx

        if ny < 0 or n <= ny or nx < 0 or m <= nx:
            continue
        if visited[ny][nx] > distance + area[ny][nx]:
            visited[ny][nx] = distance + area[ny][nx]
            heappush(queue, (distance + area[ny][nx], ny, nx))
