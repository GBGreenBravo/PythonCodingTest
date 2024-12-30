# 20241230
# 34:57
# 1 / 1

from heapq import heappop, heappush

direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
direction_knight = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def make_connected():
    start_ranges = [[(r, -1) for r in range(N)],
                    [(r, N) for r in range(N)],
                    [(-1, c) for c in range(N)],
                    [(N, c) for c in range(N)],
                    [(r, -1) for r in range(-1, N - 1)] + [(-1, c) for c in range(N - 1)],
                    [(-1, c) for c in range(1, N)] + [(r, N) for r in range(-1, N - 1)],
                    [(r, -1) for r in range(1, N + 1)] + [(N, c) for c in range(N - 1)],
                    [(r, N) for r in range(1, N + 1)] + [(N, c) for c in range(1, N)]]
    for d_idx, (dy, dx) in enumerate(direction_8):
        for sy, sx in start_ranges[d_idx]:
            y, x = sy + dy, sx + dx
            now = None
            distance = 0
            while not oob(y, x):
                if now:
                    distance += 1

                if area[y][x] != '0':
                    if not now:
                        if d_idx < 4 and area[y][x] in ('Q', 'R'):
                            now = (y, x)
                        elif d_idx >= 4 and area[y][x] in ('Q', 'B'):
                            now = (y, x)
                    else:
                        connected[now[0]][now[1]].append((y, x, distance))
                        if d_idx < 4 and area[y][x] in ('Q', 'R'):
                            now = (y, x)
                        elif d_idx >= 4 and area[y][x] in ('Q', 'B'):
                            now = (y, x)
                        else:
                            now = None
                        distance = 0
                y += dy
                x += dx


def dijkstra():
    visited = [[N**2] * N for _ in range(N)]
    visited[sy][sx] = 0
    queue = []
    for dy, dx in direction_8:
        ny, nx = sy + dy, sx + dx
        if not oob(ny, nx) and area[ny][nx] != '0':
            visited[ny][nx] = 1
            queue.append((1, ny, nx))
    while queue:
        moved, y, x = heappop(queue)

        if visited[y][x] != moved:
            continue

        if area[y][x] == 'K':
            print(moved)
            return

        if area[y][x] == 'N':
            for dy, dx in direction_knight:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] == '0' or visited[ny][nx] <= moved + 2:
                    continue
                visited[ny][nx] = moved + 2
                heappush(queue, (moved + 2, ny, nx))
        else:
            for ny, nx, added in connected[y][x]:
                if visited[ny][nx] <= moved + added:
                    continue
                visited[ny][nx] = moved + added
                heappush(queue, (moved + added, ny, nx))

    print(-1)


N = int(input())
area = [list(map(str, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 'P':
            area[i][j] = '0'
            sy, sx = i, j
            break
    else:
        continue
    break

connected = [[[] for _ in range(N)] for _ in range(N)]
make_connected()
dijkstra()
