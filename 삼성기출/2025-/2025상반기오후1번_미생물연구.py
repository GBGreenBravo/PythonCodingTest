# 20250414
# 34:55
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or N <= xx


def put():
    global group_flag
    group_flag += 1

    for i in range(r1, r2):
        for j in range(c1, c2):
            area[i][j] = group_flag

    group_visited = dict()
    visited = [[0] * N for _ in range(N)]
    group_infos = dict()
    for i in range(N):
        for j in range(N):
            if area[i][j] and not visited[i][j]:
                group_visited[area[i][j]] = group_visited.get(area[i][j], 0) + 1
                visited[i][j] = 1
                group_info = {(0, 0)}
                queue = deque()
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or area[y][x] != area[ny][nx]:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_info.add((ny - i, nx - j))
                group_infos[area[i][j]] = group_info

    separated_group_flags = set([i for i in group_visited.keys() if group_visited[i] > 1])
    for i in range(N):
        for j in range(N):
            if area[i][j] in separated_group_flags:
                area[i][j] = 1

    return dict([(i, group_infos[i]) for i in group_infos.keys() if i not in separated_group_flags])


def possible(r, c, v):
    for dr, dc in v:
        nr, nc = r + dr, c + dc
        if oob(nr, nc) or area[nr][nc]:
            return False
    return True


def move(group_infos):
    global area
    area = [[0] * N for _ in range(N)]

    sorted_group_infos = sorted(group_infos.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    for k, v in sorted_group_infos:
        for c in range(N):
            for r in range(N):
                if possible(r, c, v):
                    for dr, dc in v:
                        area[r + dr][c + dc] = k
                    break
            else:
                continue
            break


def record():
    nears = set()
    for i in range(N):
        for j in range(N):
            if area[i][j]:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if oob(ni, nj) or not area[ni][nj] or area[i][j] == area[ni][nj]:
                        continue
                    nears.add((min(area[i][j], area[ni][nj]), max(area[i][j], area[ni][nj])))

    score = 0
    for p1, p2 in nears:
        score += len(g_infos[p1]) * len(g_infos[p2])
    print(score)


N, Q = map(int, input().split())
input_arr = [tuple(map(int, input().split())) for _ in range(Q)]

area = [[0] * N for _ in range(N)]

group_flag = 0
for c1, r1, c2, r2 in input_arr:
    g_infos = put()
    move(g_infos)
    record()
