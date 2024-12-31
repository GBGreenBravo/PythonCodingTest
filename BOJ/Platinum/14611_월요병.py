# 20241231
# 16:40
# 1 / 3

from heapq import heappop, heappush

direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N + 2 <= y or x < 0 or M + 2 <= x


def dijkstra():
    visited = [[N*M*1e9] * (M + 2) for _ in range(N + 2)]
    queue = [(0, 0, 2)]
    while queue:
        cost, y, x = heappop(queue)
        if y == N + 1 or x == 0:
            print(cost)
            return

        for dy, dx in direction_8:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == -1:
                continue
            next_cost = cost
            if area[ny][nx] != -2:
                next_cost += area[ny][nx]
            if next_cost < visited[ny][nx]:
                visited[ny][nx] = next_cost
                heappush(queue, (next_cost, ny, nx))
    print(-1)


N, M = map(int, input().split())
area = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
area[0][0] = area[0][1] = area[1][0] = area[-1][-1] = area[-1][-2] = area[-2][-1] = -1
dijkstra()
