# 20241207
# 45:54
# 1 / 4

knight_direction = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
bishop_direction = ((1, 1), (1, -1), (-1, -1), (-1, 1))
rook_direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def make_connected():
    connecting = [[[[] for _ in range(3)] for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            for dy, dx in knight_direction:
                ny, nx = y + dy, x + dx
                if not oob(ny, nx):
                    connecting[y][x][0].append((ny, nx))
            for dy, dx in bishop_direction:
                ny, nx = y + dy, x + dx
                while not oob(ny, nx):
                    connecting[y][x][1].append((ny, nx))
                    ny, nx = ny + dy, nx + dx
            for dy, dx in rook_direction:
                ny, nx = y + dy, x + dx
                while not oob(ny, nx):
                    connecting[y][x][2].append((ny, nx))
                    ny, nx = ny + dy, nx + dx
    return connecting


def bfs():
    visited = [[[None] + [[0] * 3 for _ in range(N**2)] for _ in range(N)] for _ in range(N)]
    visited[sy][sx][2][0] = (0, 0)
    visited[sy][sx][2][1] = (0, 0)
    visited[sy][sx][2][2] = (0, 0)
    queue = [(sy, sx, 2, 0, 0), (sy, sx, 2, 1, 0), (sy, sx, 2, 2, 0)]
    time = 1
    while queue:
        next_queue = []
        for y, x, finding, sort, changed in queue:
            for other_sort in range(3):
                if visited[y][x][finding][other_sort] and visited[y][x][finding][other_sort][1] <= changed + 1:
                    continue
                visited[y][x][finding][other_sort] = (time, changed + 1)
                next_queue.append((y, x, finding, other_sort, changed + 1))

            for ny, nx in connected[y][x][sort]:
                if not visited[ny][nx][finding][sort]:
                    if area[ny][nx] == finding and finding != N**2 and (not visited[ny][nx][finding + 1][sort] or visited[ny][nx][finding + 1][sort][1] > changed):
                        visited[ny][nx][finding + 1][sort] = (time, changed)
                        next_queue.append((ny, nx, finding + 1, sort, changed))
                    visited[ny][nx][finding][sort] = (time, changed)
                    next_queue.append((ny, nx, finding, sort, changed))
                else:
                    origin_time, origin_changed = visited[ny][nx][finding][sort]
                    if origin_time == time and origin_changed > changed:
                        if area[ny][nx] == finding and finding != N**2 and (not visited[ny][nx][finding + 1][sort] or visited[ny][nx][finding + 1][sort][1] > changed):
                            visited[ny][nx][finding + 1][sort] = (time, changed)
                            next_queue.append((ny, nx, finding + 1, sort, changed))
                        visited[ny][nx][finding][sort] = (time, changed)
                        next_queue.append((ny, nx, finding, sort, changed))

        if sum(bool(v) for v in visited[ey][ex][N**2]):
            print(*min([v for v in visited[ey][ex][N**2] if v]))
            return

        time += 1
        queue = next_queue


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            sy, sx = i, j
        elif area[i][j] == N**2:
            ey, ex = i, j
connected = make_connected()
bfs()
