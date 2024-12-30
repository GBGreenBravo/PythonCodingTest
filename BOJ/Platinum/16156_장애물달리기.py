# 20241230
# 38:53
# 1 / 3

from heapq import heappush, heappop

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def dijkstra():
    result = [0] * N

    visited = [[5e6] * M for _ in range(N)]
    queue = []
    for r in range(N):
        visited[r][M - 1] = area[r][M - 1]
        heappush(queue, (area[r][M - 1], r, M - 1, r))

    while queue:
        distance, y, x, last_col = heappop(queue)

        if visited[y][x] != distance:
            continue

        if x == 0:
            result[last_col] += 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            next_distance = distance + area[ny][nx]
            if next_distance < visited[ny][nx]:
                visited[ny][nx] = next_distance
                heappush(queue, (next_distance, ny, nx, last_col))

    return result


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
print(*dijkstra(), sep="\n")
