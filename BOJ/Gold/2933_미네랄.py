# 20241010
# 23:04
# 1 / 2

# 부서지는 좌표 상하좌우에서 방문된 곳 재방문하면 안됐는데, 방문 가능하게 구현해서 한번 틀렸음.
# if oob(nsy, nsx) or area[nsy][nsx] == '.':
# 위 코드를 아래로 수정
# if oob(nsy, nsx) or area[nsy][nsx] == '.' or visited[nsy][nsx]:

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


def break_mineral(sy, sx):
    area[sy][sx] = '.'

    visited = [[0] * c for _ in range(r)]
    visited[sy][sx] = 1

    for dsy, dsx in direction:
        nsy, nsx = sy + dsy, sx + dsx
        if oob(nsy, nsx) or area[nsy][nsx] == '.' or visited[nsy][nsx]:
            continue

        visited[nsy][nsx] = 1

        queue = deque()
        queue.append((nsy, nsx))

        now_group = [(nsy, nsx)]

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == '.':
                    continue
                visited[ny][nx] = 1
                queue.append((ny, nx))

                now_group.append((ny, nx))

        below_rows = [-1] * c
        for gy, gx in now_group:
            below_rows[gx] = max(below_rows[gx], gy)

        falling_height = r
        for col_idx, below_row in enumerate(below_rows):
            if below_row == -1:
                continue
            if below_row == r - 1:
                falling_height = 0
                break

            fy, fx = below_row + 1, col_idx
            while not oob(fy, fx) and area[fy][fx] == '.':
                fy += 1

            fy -= 1
            falling_height = min(falling_height, fy - below_row)

        if not falling_height:
            continue

        for gy, gx in now_group:
            area[gy][gx] = '.'
        for gy, gx in now_group:
            area[gy + falling_height][gx] = 'x'
        return


r, c = map(int, input().split())
area = [list(str(input())) for _ in range(r)]
throwing_cnt = int(input())
throwing_rows = list(map(lambda inp: r - int(inp), input().split()))

for throwing_idx, throwing_row in enumerate(throwing_rows):
    if not throwing_idx % 2:
        ti, tj, dtj = throwing_row, 0, 1
    else:
        ti, tj, dtj = throwing_row, c - 1, -1

    while not oob(ti, tj):
        if area[ti][tj] == 'x':
            break_mineral(ti, tj)
            break
        tj += dtj

for area_row in area:
    print(*area_row, sep="")
