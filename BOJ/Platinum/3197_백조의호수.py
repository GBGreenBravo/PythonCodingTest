# 20241126
# 35:41
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or R <= y or x < 0 or C <= x


def find():
    f, s = None, None
    for y in range(R):
        for x in range(C):
            if area[y][x] == 'L':
                if not f:
                    area[y][x] = '.'
                    f = (y, x)
                else:
                    area[y][x] = '.'
                    s = (y, x)
                    return f, s


def cal_first_melt():
    melt = set()
    visited = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if area[y][x] == '.' and not visited[y][x]:
                visited[y][x] = 1
                queue = deque()
                queue.append((y, x))

                while queue:
                    cy, cx = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = cy + dy, cx + dx
                        if oob(ny, nx) or visited[ny][nx]:
                            continue
                        if area[ny][nx] != '.':
                            if area[ny][nx] == 'X':
                                melt.add((ny, nx))
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    return melt


def carve():
    area[first[0]][first[1]] = 1
    queue = deque([first])
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] != '.':
                continue
            area[ny][nx] = 1
            queue.append((ny, nx))

    area[second[0]][second[1]] = 2
    queue = deque([second])
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] != '.':
                continue
            area[ny][nx] = 2
            queue.append((ny, nx))


def solve():
    global melting

    days = 1

    while melting:
        next_melting = set()
        for y, x in melting:
            area[y][x] = '.'

            nears = [None] * 4
            for d_idx, (dy, dx) in enumerate(direction):
                ny, nx = y + dy, x + dx
                if oob(ny, nx):
                    continue
                nears[d_idx] = area[ny][nx]
                if (ny, nx) in melting:
                    continue
                if area[ny][nx] == 'X':
                    next_melting.add((ny, nx))

            if 1 in nears and 2 in nears:
                print(days)
                return
            elif 1 in nears:
                area[y][x] = 1
                for d_idx, (dy, dx) in enumerate(direction):
                    if nears[d_idx] == '.':
                        sy, sx = y + dy, x + dx
                        area[sy][sx] = 1
                        queue = deque()
                        queue.append((sy, sx))
                        while queue:
                            yy, xx = queue.popleft()
                            for dyy, dxx in direction:
                                nyy, nxx = yy + dyy, xx + dxx
                                if oob(nyy, nxx) or area[nyy][nxx] != '.':
                                    continue
                                area[nyy][nxx] = 1
                                queue.append((nyy, nxx))
            elif 2 in nears:
                area[y][x] = 2
                for d_idx, (dy, dx) in enumerate(direction):
                    if nears[d_idx] == '.':
                        sy, sx = y + dy, x + dx
                        area[sy][sx] = 2
                        queue = deque()
                        queue.append((sy, sx))
                        while queue:
                            yy, xx = queue.popleft()
                            for dyy, dxx in direction:
                                nyy, nxx = yy + dyy, xx + dxx
                                if oob(nyy, nxx) or area[nyy][nxx] != '.':
                                    continue
                                area[nyy][nxx] = 2
                                queue.append((nyy, nxx))

        melting = next_melting
        days += 1


R, C = map(int, input().split())
area = [list(str(input())) for _ in range(R)]
first, second = find()

melting = cal_first_melt()
carve()
solve()
