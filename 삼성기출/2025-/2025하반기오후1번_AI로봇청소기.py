# 20250929
# 44:29
# 1 / 2

# directions 설정 실수; 좌상우하를 좌상하우로 잘못 씀

direction = ((0, -1), (-1, 0), (0, 1), (1, 0))  # 좌 상 우 하


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or N <= xx


def find_next(sy, sx):
    if area[sy][sx] > 0:
        return sy, sx

    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1

    queue = [(sy, sx)]
    while queue:
        next_queue = []
        poss = []
        for y, x in queue:
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] == -1 or visited[ny][nx] or (ny, nx) in robots_set:
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))
                if area[ny][nx] > 0:
                    poss.append((ny, nx))
        if poss:
            return min(poss, key=lambda yx:(yx[0], yx[1]))
        else:
            queue = next_queue

    return sy, sx


def move_robots():
    for ii in range(K):
        si, sj = robots[ii]
        ni, nj = find_next(si, sj)

        robots_set.remove((si, sj))
        robots[ii] = (ni, nj)
        robots_set.add((ni, nj))


def clean():
    for ii in range(K):
        y, x = robots[ii]
        near = [0] * 5
        near[-1] = min(area[y][x], 20)
        area[y][x] -= min(area[y][x], 20)
        for di, (dy, dx) in enumerate(direction):
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == -1: continue
            near[di] = min(area[y + dy][x + dx], 20)
            area[ny][nx] -= min(area[ny][nx], 20)

        candidates = []
        for jj in range(4):
            candidates.append(sum(near) - near[jj])
        r = candidates.index(max(candidates))
        ry, rx = y + direction[r][0], x + direction[r][1]
        if not(oob(ry, rx)) and area[ry][rx] != -1:
            area[ry][rx] += near[r]


def add_dust():
    for y in range(N):
        for x in range(N):
            if area[y][x] > 0:
                area[y][x] += 5


def spread_dust():
    added = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not area[y][x]:
                add = 0
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or area[ny][nx] <= 0:
                        continue
                    add += area[ny][nx]
                added[y][x] = add // 10
    for y in range(N):
        for x in range(N):
            if added[y][x]:
                area[y][x] += added[y][x]


N, K, L = map(int, input().split())
area = [[0] * N for _ in range(N)]
for i in range(N):
    area[i] = list(map(int, input().split()))
robots = list()
robots_set = set()
for k in range(K):
    robots.append(tuple(map(lambda yx: int(yx) - 1, input().split())))
    robots_set.add(robots[-1])

for _ in range(L):
    move_robots()
    clean()
    add_dust()
    spread_dust()
    print(sum([sum([j for j in area[i] if j != -1]) for i in range(N)]))
