from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob_area(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def oob_dimension3(y, x):
    if y < 0 or 3 * M <= y or x < 0 or 3 * M <= x:
        return True
    if y < M and x < M:
        return True
    if y < M and x >= 2 * M:
        return True
    if y >= 2 * M and x < M:
        return True
    if y >= 2 * M and x >= 2 * M:
        return True
    return False


def find_exit_index():
    dimension_exit_index, area_exit_index = None, None
    final_exit_index = None
    for sy in range(N):
        for sx in range(N):
            if not dimension_exit_index and area[sy][sx] == 3:
                for d in range(M):
                    for y, x in ((sy + d, sx), (sy, sx + d), (sy + M - 1 - d, sx + M - 1), (sy + M - 1, sx + M - 1 - d)):
                        for dy, dx in direction:
                            ny, nx = y + dy, x + dx
                            if not oob_area(ny, nx) and area[ny][nx] in (0, 4):
                                area_exit_index = ny, nx
                                if ny < sy:
                                    dimension_exit_index = 0, M + x - sx
                                elif ny >= sy + M:
                                    dimension_exit_index = 3 * M - 1, M + x - sx
                                elif nx < sx:
                                    dimension_exit_index = M + y - sy, 0
                                elif nx >= sx + M:
                                    dimension_exit_index = M + y - sy, 3 * M - 1
                        if dimension_exit_index:
                            break
                    else:
                        continue
                    break
            if area[sy][sx] == 4:
                final_exit_index = sy, sx
    return dimension_exit_index, area_exit_index, final_exit_index


def make_dimension3_connected():
    connected = [[[] for _ in range(3 * M)] for _ in range(3 * M)]
    for y in range(3 * M):
        for x in range(3 * M):
            if oob_dimension3(y, x):
                continue
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if not oob_dimension3(ny, nx):
                    connected[y][x].append((ny, nx))
    for d in range(M):
        connected[d][M].append((M, d))
        connected[M][d].append((d, M))

        connected[d][2 * M - 1].append((M, 3 * M - 1 - d))
        connected[M][3 * M - 1 - d].append((d, 2 * M - 1))

        connected[3 * M - 1 - d][M].append((2 * M - 1, d))
        connected[2 * M - 1][d].append((3 * M - 1 - d, M))

        connected[3 * M - 1 - d][2 * M - 1].append((2 * M - 1, 3 * M - 1 - d))
        connected[2 * M - 1][3 * M - 1 - d].append((3 * M - 1 - d, 2 * M - 1))
    return connected


def distort_area(turn):
    global phenomena

    next_phenomena = []
    for py, px, pd, pv in phenomena:
        if turn % pv:
            next_phenomena.append((py, px, pd, pv))
            continue

        npy, npx = py + direction[pd][0], px + direction[pd][1]
        if oob_area(npy, npx) or area[npy][npx] in (1, 3, 4):
            continue
        else:
            area[npy][npx] = -1
            next_phenomena.append((npy, npx, pd, pv))
    phenomena = next_phenomena


def find_start_point():
    for y in range(3 * M):
        for x in range(3 * M):
            if dimension3[y][x] == 2:
                dimension3[y][x] = 0
                return y, x


def escape():
    turn = 1

    queue = deque()

    sy, sx = find_start_point()
    visited_dimension3[sy][sx] = turn
    queue.append((False, sy, sx))

    while queue:
        distort_area(turn)

        next_queue = deque()
        while queue:
            on_area, y, x = queue.popleft()
            if not on_area:
                if (y, x) == dimension_exit:
                    ay, ax = area_exit
                    if area[ay][ax] in (0, 4):
                        visited_area[ay][ax] = turn + 1
                        next_queue.append((True, *area_exit))
                    continue

                for ny, nx in dimension3_connected[y][x]:
                    if visited_dimension3[ny][nx] or dimension3[ny][nx]:
                        continue
                    visited_dimension3[ny][nx] = turn + 1
                    next_queue.append((False, ny, nx))
            else:  # if on_area:
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob_area(ny, nx) or visited_area[ny][nx] or area[ny][nx] in (-1, 1, 3):
                        continue
                    visited_area[ny][nx] = turn + 1
                    next_queue.append((True, ny, nx))

        if visited_area[final_exit[0]][final_exit[1]]:
            return

        queue = next_queue
        turn += 1


N, M, F = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

dimension_exit, area_exit, final_exit = find_exit_index()

east = [list(map(int, input().split())) for _ in range(M)]
east = [list(row) for row in list(zip(*east))[::-1]]
west = [list(map(int, input().split())) for _ in range(M)]
west = [list(row)[::-1] for row in zip(*west)]
south = [list(map(int, input().split())) for _ in range(M)]
north = [list(map(int, input().split())) for _ in range(M)]
north = [list(row)[::-1] for row in north[::-1]]
upper = [list(map(int, input().split())) for _ in range(M)]

dimension3 = [[0] * (3 * M) for _ in range(3 * M)]
for i in range(M):
    for j in range(M):
        dimension3[i][M + j] = north[i][j]
        dimension3[M + i][j] = west[i][j]
        dimension3[M + i][M + j] = upper[i][j]
        dimension3[M + i][2 * M + j] = east[i][j]
        dimension3[2 * M + i][M + j] = south[i][j]
dimension3_connected = make_dimension3_connected()

phenomena = []
for _ in range(F):
    rr, cc, dd, vv = map(int, input().split())
    area[rr][cc] = -1
    phenomena.append((rr, cc, dd, vv))

visited_area = [[0] * N for _ in range(N)]
visited_dimension3 = [[0] * (3 * M) for _ in range(3 * M)]
escape()
print(visited_area[final_exit[0]][final_exit[1]] - 1)
