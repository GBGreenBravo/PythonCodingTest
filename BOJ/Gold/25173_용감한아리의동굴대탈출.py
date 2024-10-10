# 20241010
# 1:02:51
# 1 / 3

# 1. 아리 이동 시, 방향 안 바꿔줘서 1번 틀림.
# 2. 나선형 탐색에서 while문 조건으로 sum(map(lambda vis_row: vis_row.count(0), visited))를 써서 시간초과 났음.

from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
ari_life, ari_power, boss_life, boss_power = map(int, input().split())

for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            ari_y, ari_x = i, j
        elif area[i][j] == 3:
            boss_y, boss_x = i, j
            for d_idx, (di, dj) in enumerate(direction):
                ni, nj = i + di, j + dj
                if not oob(ni, nj) and area[ni][nj] == 2:
                    ari_d, boss_d = d_idx, d_idx
area[ari_y][ari_x] = 0
area[boss_y][boss_x] = 0

while ari_life > 0 and boss_life > 0:
    # 아리 공격
    boss_life -= ari_power
    if boss_life <= 0:
        break

    # 아리 이동
    ari_before_y, ari_before_x = ari_y, ari_x

    day, dax = direction[ari_d]
    any, anx = ari_y + day, ari_x + dax
    for _ in range(4):
        if oob(any, anx) or area[any][anx] == 1 or (any == boss_y and anx == boss_x):
            ari_life -= 1
            ari_d = (ari_d + 1) % 4
            day, dax = direction[ari_d]
            any, anx = ari_y + day, ari_x + dax
            continue
        ari_y, ari_x = any, anx
        break

    if ari_life <= 0:
        break

    # 보스 공격
    visited = [[0] * m for _ in range(n)]
    visited[boss_y][boss_x] = 1
    visited_cnt = 1

    sy, sx, sd = boss_y, boss_x, boss_d
    now_dist = 0
    dist_limit = 1
    undermon = None
    # while sum(map(lambda vis_row: vis_row.count(0), visited)):  # 시간초과 났던 포인트
    while visited_cnt != n * m:
        if now_dist == dist_limit:
            sd = (sd + 1) % 4
        elif now_dist == dist_limit * 2:
            sd = (sd + 1) % 4
            now_dist = 0
            dist_limit += 1

        sy, sx = sy + direction[sd][0], sx + direction[sd][1]
        if not oob(sy, sx) and area[sy][sx] == 1:
            undermon = sy, sx
            break
        if not oob(sy, sx):
            visited[sy][sx] = 1
            visited_cnt += 1
        now_dist += 1

    if undermon:
        usy, usx = undermon
        visited = [[0] * m for _ in range(n)]
        visited[usy][usx] = boss_power

        queue = deque()
        queue.append((usy, usx))

        while queue:
            uy, ux = queue.popleft()
            remain = visited[uy][ux]

            if remain == 1:
                break

            for duy, dux in direction:
                nuy, nux = uy + duy, ux + dux
                if oob(nuy, nux) or visited[nuy][nux] or (nuy == boss_y and nux == boss_x):
                    continue
                if nuy == ari_y and nux == ari_x:
                    visited[ari_y][ari_x] = remain - 1
                    break
                if area[nuy][nux] == 0:
                    visited[nuy][nux] = remain - 1
                    queue.append((nuy, nux))
            else:
                continue
            break

        ari_life -= visited[ari_y][ari_x]
        if ari_life <= 0:
            break

    # 보스 이동
    if not (ari_y == ari_before_y and ari_x == ari_before_x):
        boss_y, boss_x = ari_before_y, ari_before_x
        boss_d = ari_d

print("VICTORY!" if ari_life > 0 else "CAVELIFE...")
