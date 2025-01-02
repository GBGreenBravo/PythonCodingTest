# 20250102
# 45:59
# 1 / 1

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
o_move = (None,
          ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)),
          ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0)),
          ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)),
          ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)),
          ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0), (9, 0), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs():
    visited = [[[0] * 480 for _ in range(M)] for _ in range(N)]
    visited[sy][sx][0] = 1

    queue = [(sy, sx)]

    time = 1
    while queue:
        next_queue = []
        for y, x in queue:
            if y == ey and x == ex:
                print((time - 1) // 2)
                return

            if not y % 2 and not x % 2:
                if not visited[y][x][(time - 1) % 480]:
                    for d in range(1, 6):
                        ody, odx = o_move[d][(time - 1) % (8 * d)]
                        oy, ox = y - ody, x - odx
                        if not oob(oy, ox) and d in obstacles[oy][ox]:
                            break
                    else:
                        visited[y][x][(time - 1) % 480] = 1
                        next_queue.append((y, x))
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx][time % 480] or area[ny][nx]:
                        continue
                    for d in range(1, 6):
                        ody, odx = o_move[d][time % (8 * d)]
                        oy, ox = ny - ody, nx - odx
                        if not oob(oy, ox) and d in obstacles[oy][ox]:
                            break
                    else:
                        visited[ny][nx][time % 480] = 1
                        next_queue.append((ny, nx))
            else:
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx][time % 480] or area[ny][nx] or (ny % 2 and nx % 2):
                        continue
                    for d in range(1, 6):
                        ody, odx = o_move[d][time % (8 * d)]
                        oy, ox = ny - ody, nx - odx
                        if not oob(oy, ox) and d in obstacles[oy][ox]:
                            break
                    else:
                        visited[ny][nx][time % 480] = 1
                        next_queue.append((ny, nx))

        time += 1
        queue = next_queue

    print("INF")


input_N, input_M = map(lambda inp: int(inp) + 1, input().split())
input_area = [list(str(input())) for _ in range(input_N)]
N, M = input_N * 2 - 1, input_M * 2 - 1
area = [[0] * M for _ in range(N)]
for i in range(input_N):
    for j in range(input_M):
        if input_area[i][j] == 'S':
            sy, sx = i * 2, j * 2
        elif input_area[i][j] == 'E':
            ey, ex = i * 2, j * 2
        elif input_area[i][j] == '#':
            area[i * 2][j * 2] = 1
obstacles = [[[] for _ in range(M)] for _ in range(N)]
K = int(input())
for _ in range(K):
    aa, bb, cc = map(int, input().split())
    obstacles[bb * 2][cc * 2].append(aa)
bfs()
