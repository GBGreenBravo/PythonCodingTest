# 20241227
# 21:47
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def bfs():
    visited = [[[[0] * 4 for _ in range(14)] for _ in range(N)] for _ in range(N)]
    for d_idx in range(4):
        visited[0][0][0][d_idx] = 1
    queue = [(0, 0, 0, 0)]
    time = 0
    while queue:
        next_queue = []
        for y, x, before_dist, before_idx in queue:
            if y == N - 1 and x == N - 1:
                print(time)
                return

            for d_idx, (dy, dx) in enumerate(direction):
                if d_idx == before_idx:
                    now_dist = before_dist + 1
                    ny, nx = y + dy * now_dist, x + dx * now_dist
                    if oob(ny, nx) or visited[ny][nx][now_dist][d_idx]:
                        continue
                    if 0 < area[ny][nx] <= time + 1:
                        continue
                    cy, cx = y + dy, x + dx
                    while cy != ny or cx != nx:
                        if 0 < area[cy][cx] <= time:
                            break
                        cy, cx = cy + dy, cx + dx
                    else:
                        visited[ny][nx][now_dist][d_idx] = 1
                        next_queue.append((ny, nx, now_dist, d_idx))

                else:
                    now_dist = 1
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx][now_dist][d_idx]:
                        continue
                    if 0 < area[ny][nx] <= time + 1:
                        continue
                    visited[ny][nx][now_dist][d_idx] = 1
                    next_queue.append((ny, nx, now_dist, d_idx))

        queue = next_queue
        time += 1

    print("Fired")


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
bfs()
