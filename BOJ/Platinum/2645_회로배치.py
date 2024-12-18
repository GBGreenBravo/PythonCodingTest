# 20241218
# 27:48
# 1 / 1

from heapq import heappop, heappush

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def carve(y1, x1, y2, x2):
    if y1 == y2:
        d = 0 if x1 < x2 else 1
    else:
        d = 2 if y1 < y2 else 3
    dy, dx = direction[d]
    area[y1][x1] = 1
    while y1 != y2 or x1 != x2:
        y1, x1 = y1 + dy, x1 + dx
        area[y1][x1] = 1


def print_route(route):
    points = [(sy, sx)]
    idx = 1
    while idx != len(route):
        if idx == 1:
            (y1, x1), (y2, x2) = route[idx], route[idx - 1]
            if y1 == y2:
                bd = 0 if x1 < x2 else 1
            else:
                bd = 2 if y1 < y2 else 3
            idx += 1
            continue
        (y1, x1), (y2, x2) = route[idx], route[idx - 1]
        if y1 == y2:
            d = 0 if x1 < x2 else 1
        else:
            d = 2 if y1 < y2 else 3
        if d != bd:
            points.append(route[idx - 1])
            bd = d
        idx += 1
    points.append((ey, ex))
    print(len(points), end=" ")
    for py, px in points:
        print(py + 1, px + 1, end=" ")


def dijkstra():
    visited = [[N**2 * K] * N for _ in range(N)]
    visited[sy][sx] = K if area[sy][sx] else 1
    pq = [(K if area[sy][sx] else 1, sy, sx, [(sy, sx)])]
    while pq:
        cost, y, x, route = heappop(pq)
        if visited[y][x] != cost:
            continue
        if y == ey and x == ex:
            print(cost)
            print_route(route)
            return
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            next_cost = cost
            next_cost += K if area[ny][nx] else 1
            if visited[ny][nx] <= next_cost:
                continue
            visited[ny][nx] = next_cost
            heappush(pq, (next_cost, ny, nx, route + [(ny, nx)]))


N = int(input())
sy, sx, ey, ex = map(lambda inp: int(inp) - 1, input().split())
K = int(input())
M = int(input())
area = [[0] * N for _ in range(N)]
for _ in range(M):
    lst = list(map(lambda inp: int(inp) - 1, input().split()))
    for i in range(1, lst[0] * 2, 2):
        carve(lst[i], lst[i + 1], lst[i + 2], lst[i + 3])

dijkstra()
