# 20240928
# 58:05
# 1 / 6

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


def fall(sy, sx):
    visited = [[0] * c for _ in range(r)]
    visited[sy][sx] = 1

    for dsy, dsx in direction:
        falling_possible = False

        nsy, nsx = sy + dsy, sx + dsx
        if not oob(nsy, nsx) and not visited[nsy][nsx] and area[nsy][nsx] == 'x' and nsy != r - 1:
            visited[nsy][nsx] = 1

            queue = deque()
            queue.append((nsy, nsx))

            now_group = [(nsy, nsx)]
            falling_possible = True

            while queue:
                y, x = queue.popleft()
                for dy, dx, in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == '.':
                        continue
                    if ny == r - 1:
                        falling_possible = False
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    now_group.append((ny, nx))

            if falling_possible:
                break

    if not falling_possible:
        return

    falling_height = r
    for gy, gx in now_group:
        h = 1
        while gy + h < r and (area[gy + h][gx] == '.' or (gy + h, gx) in now_group):
            h += 1
        falling_height = min(falling_height, h - 1)

    now_group.sort(reverse=True)
    for fy, fx in now_group:
        area[fy + falling_height][fx] = 'x'
        area[fy][fx] = '.'


r, c = map(int, input().split())
area = [list(str(input())) for _ in range(r)]

throwing_cnt = int(input())
throwing_rows = [None] + list(map(lambda tt: r - int(tt), input().split()))

for throwing_number in range(1, throwing_cnt + 1):
    dtx = 1 if throwing_number % 2 else -1

    ty = throwing_rows[throwing_number]
    tx = 0 if throwing_number % 2 else c - 1

    while not oob(ty, tx):
        if area[ty][tx] == 'x':
            area[ty][tx] = '.'
            fall(ty, tx)
            break

        tx += dtx

for row in area:
    print(*row, sep="")
