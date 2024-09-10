# 20240910
# 27:00
# 1 / 1

"""
풀이 시간: 27분 (14:04 ~ 14:31)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:04 - 14:)


2. 구현 (14: - 14:)


3. 검증 (14: - 14:31)
"""

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동 남 서 북


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


def roll_dice(now_dice, dice_direction_idx):
    down, up, east, west, south, north = now_dice
    if dice_direction_idx == 0:
        return east, west, up, down, south, north
    elif dice_direction_idx == 1:
        return south, north, east, west, up, down
    elif dice_direction_idx == 2:
        return west, east, down, up, south, north
    else:
        return north, south, east, west, down, up


def cal_score(sy, sx):
    criteria = area[sy][sx]

    visited = [[0] * m for _ in range(n)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for ddy, ddx in direction:
            nny, nnx = y + ddy, x + ddx
            if oob(nny, nnx) or visited[nny][nnx] or area[nny][nnx] != criteria:
                continue
            visited[nny][nnx] = 1
            queue.append((nny, nnx))

    return criteria * sum(map(sum, visited))


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dice_y, dice_x = 0, 0
dice_d = 0
dice = (6, 1, 3, 4, 5, 2)  # 아래/위/동/서/남/북

total_score = 0

for _ in range(k):
    dy, dx = direction[dice_d]
    ny, nx = dice_y + dy, dice_x + dx
    if oob(ny, nx):
        ny, nx = dice_y - dy, dice_x - dx
        dice_d = (dice_d + 2) % 4

    dice_y, dice_x = ny, nx
    dice = roll_dice(dice, dice_d)

    B = area[dice_y][dice_x]
    total_score += cal_score(dice_y, dice_x)
    A = dice[0]
    if A > B:
        dice_d += 1
        dice_d %= 4
    elif A < B:
        dice_d -= 1
        dice_d %= 4

print(total_score)
