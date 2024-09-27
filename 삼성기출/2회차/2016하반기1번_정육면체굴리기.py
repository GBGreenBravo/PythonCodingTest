# 20240927
# 12:36
# 1 / 1

# 14499_주사위굴리기

"""
풀이 시간: 13분 (16:16 - 16:29)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:17 - 16:20)
    (09/27 한정) 정독&메모 하지 않았습니다..
    문제 정독&메모 루틴의 소중함을 깨달은 하루였습니다.


2. 구현 (16:20 - 16:28)
    처음에 접했던, "14499_주사위굴리기" 문제에서 고전했던 경험이 있었기에,
    풀이법이 바로 기억났고 그대로 구현했습니다.

    하나 가져갈 점은, 이제 주사위 굴리는 유형이 나온다면,
    "아래/위/동/서/북/남"으로 이제껏 구현했기에, 이 index 순서를 그대로 적용할 것입니다.


3. 디버깅 (-)
"""

direction = (None, (0, 1), (0, -1), (-1, 0), (1, 0))  # 동 서 북 남


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


def roll(direction_idx):
    global dice

    bottom, top, east, west, north, south = dice

    if direction_idx == 1:
        dice = [east, west, top, bottom, north, south]
    elif direction_idx == 2:
        dice = [west, east, bottom, top, north, south]
    elif direction_idx == 3:
        dice = [north, south, east, west, top, bottom]
    elif direction_idx == 4:
        dice = [south, north, east, west, bottom, top]
    else:
        print('not here')


n, m, sy, sx, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 아래/위/동/서/북/남
# 0  1  2  3  4  5
dice = [0, 0, 0, 0, 0, 0]
y, x = sy, sx

for d_idx in commands:
    dy, dx = direction[d_idx]
    ny, nx = y + dy, x + dx

    if oob(ny, nx):
        continue

    y, x = ny, nx

    roll(d_idx)

    if not area[y][x]:
        area[y][x] = dice[0]
    else:
        dice[0] = area[y][x]
        area[y][x] = 0

    print(dice[1])
