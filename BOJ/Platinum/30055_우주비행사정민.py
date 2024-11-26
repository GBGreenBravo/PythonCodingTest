# 20241126
# 1:10:42
# 1 / 4

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def make_next_areas():
    i, j, d = 0, 1, 1
    next_area1[0][0] = (0, 1)
    while not (i == N1 - 1 and j == 0):
        if j == M1 - 1 and d == 1:
            next_area1[i][j] = (i + 1, j)
            i += 1
            d = -1
        elif j == 0 and d == -1:
            next_area1[i][j] = (i + 1, j)
            i += 1
            d = 1
        else:
            next_area1[i][j] = (i, j + d)
            j += d
    next_area1[-1][0] = (0, 0)

    i, j, d = 0, 1, 1
    next_area2[0][0] = (0, 1)
    while not (i == N2 - 1 and j == 0):
        if j == M2 - 1 and d == 1:
            next_area2[i][j] = (i + 1, j)
            i += 1
            d = -1
        elif j == 0 and d == -1:
            next_area2[i][j] = (i + 1, j)
            i += 1
            d = 1
        else:
            next_area2[i][j] = (i, j + d)
            j += d
    next_area2[-1][0] = (0, 0)


def spread_black_holes():
    global black_holes

    next_black_holes = []
    for area_num, y, x in black_holes:
        if area_num == 1:
            ny, nx = next_area1[y][x]
            if area1[ny][nx] == 1:
                continue
            area1[ny][nx] = 1
            next_black_holes.append((1, ny, nx))
        else:
            ny, nx = next_area2[y][x]
            if area2[ny][nx] == 1:
                continue
            area2[ny][nx] = 1
            next_black_holes.append((2, ny, nx))
    black_holes = next_black_holes


def oob1(y, x):
    return y < 0 or N1 <= y or x < 0 or M1 <= x


def oob2(y, x):
    return y < 0 or N2 <= y or x < 0 or M2 <= x


def bfs():
    visited1 = [[0] * M1 for _ in range(N1)]
    visited1[0][0] = 1
    visited2 = [[0] * M2 for _ in range(N2)]
    queue = []
    queue.append((1, 0, 0, 0))  # areaNum, y, x, left_time(이동중)

    time = 0
    while queue:
        next_queue = []
        for area_num, y, x, left_time in queue:
            if left_time:
                next_queue.append((area_num, y, x, left_time - 1))
                if left_time == 1:
                    if area_num == 1:
                        visited1[y][x] = 1
                    else:
                        visited2[y][x] = 1
                continue

            if area_num == 1:
                if area1[y][x] == 1:
                    continue
                if area1[y][x] == 2:
                    ny, nx = connected1[(y, x)]
                    if not visited2[ny][nx]:
                        next_queue.append((2, ny, nx, 2))
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob1(ny, nx) or visited1[ny][nx] or area1[ny][nx] == 1:
                        continue
                    visited1[ny][nx] = 1
                    next_queue.append((1, ny, nx, 0))

            else:  # elif area_num == 2:
                if area2[y][x] == 1:
                    continue
                if y == N2 - 1 and x == M2 - 1:
                    print(time)
                    return
                if area2[y][x] == 2:
                    ny, nx = connected2[(y, x)]
                    if not visited1[ny][nx]:
                        next_queue.append((1, ny, nx, 2))
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob2(ny, nx) or visited2[ny][nx] or area2[ny][nx] == 1:
                        continue
                    visited2[ny][nx] = 1
                    next_queue.append((2, ny, nx, 0))

        spread_black_holes()

        if next_queue:
            queue = next_queue
            time += 1
        else:
            break
    print("hing...")


K, N1, M1, N2, M2 = map(int, input().split())
area1 = [[0] * M1 for _ in range(N1)]
area2 = [[0] * M2 for _ in range(N2)]
A, B = map(int, input().split())
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
connected1 = dict()
connected2 = dict()
for i in range(A):
    for j in range(B):
        area1[R1 + i][C1 + j] = 2
        area2[R2 + i][C2 + j] = 2
        connected1[(R1 + i, C1 + j)] = (R2 + i, C2 + j)
        connected2[(R2 + i, C2 + j)] = (R1 + i, C1 + j)

black_holes = []
for _ in range(K):
    dd, dr, dc = map(int, input().split())
    if dd == 1:
        area1[dr][dc] = 1
    else:  # elif dd == 2:
        area2[dr][dc] = 1
    black_holes.append((dd, dr, dc))

next_area1 = [[None] * M1 for _ in range(N1)]
next_area2 = [[None] * M2 for _ in range(N2)]
make_next_areas()

bfs()
