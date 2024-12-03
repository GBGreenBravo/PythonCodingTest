# 20241203
# 47:49
# 1 / 4

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or R <= y or x < 0 or C <= x


def find_minimum_dists():
    dist_arr = [0] * N
    visited = [[0] * C for _ in range(R)]
    visited[ey][ex] = 1
    queue = deque()
    queue.append((ey, ex, 1))
    while queue:
        y, x, distance = queue.popleft()
        if y * C + x in pieces_set:
            dist_arr[pieces_dict[y * C + x]] = distance - 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx, distance + 1))

    return dist_arr, visited


def cal_start_from(sy, sx):
    visited = [[0] * C for _ in range(R)]
    visited[sy][sx] = 1
    queue = deque()
    queue.append((sy, sx, 1))
    while queue:
        y, x, distance = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx, distance + 1))

    return visited


def find_candidates():
    candis = []
    visited = [[0] * C for _ in range(R)]
    visited[ey][ex] = 1
    queue = deque()
    queue.append((ey, ex))
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            if area[ny][nx]:
                candis.append((ny, nx))
                continue
            queue.append((ny, nx))
    return candis


def cal_wall_value(sy, sx):
    near_indexes = []
    for dy, dx in direction:
        ny, nx = sy + dy, sx + dx
        if not oob(ny, nx) and not area[ny][nx]:
            near_indexes.append((ny, nx))

    now_value = 0
    for p in range(N):
        start_lengths = [1e5]
        for y, x in near_indexes:
            if start_from_pieces[p][y][x]:
                start_lengths.append(start_from_pieces[p][y][x])
        end_lengths = [1e5]
        for y, x in near_indexes:
            if start_from_e[y][x]:
                end_lengths.append(start_from_e[y][x])

        tmp_value = m_dists[p] - (min(start_lengths) + min(end_lengths))
        if tmp_value > 0:
            now_value += tmp_value
    return now_value


T = int(input())
for _ in range(T):
    R, C, N, ey, ex = map(int, input().split())
    ey, ex = ey - 1, ex - 1

    pieces_set = set()
    pieces_dict = dict()
    for i in range(N):
        aa, bb = map(lambda inp: int(inp) - 1, input().split())
        pieces_set.add(aa * C + bb)
        pieces_dict[aa * C + bb] = i

    area = [[int(i == 'W') for i in str(input())] for _ in range(R)]

    m_dists, start_from_e = find_minimum_dists()
    origin_value = sum(m_dists)

    start_from_pieces = [None] * N
    for piece in pieces_set:
        start_from_pieces[pieces_dict[piece]] = cal_start_from(*divmod(piece, C))

    candidates = find_candidates()
    wall_value = 0
    for i, j in candidates:
        wall_value += cal_wall_value(i, j)

    print(origin_value, wall_value)
