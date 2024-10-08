# 20241008
# 30:06
# 1 / 1

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def convert_direction(direction_idx, triangle):
    if direction_idx == 0:
        if triangle == 1:
            return 2
        elif triangle == 2:
            return 2
        elif triangle == 3:
            return 1
        elif triangle == 4:
            return 3
    elif direction_idx == 1:
        if triangle == 1:
            return 0
        elif triangle == 2:
            return 3
        elif triangle == 3:
            return 3
        elif triangle == 4:
            return 2
    elif direction_idx == 2:
        if triangle == 1:
            return 3
        elif triangle == 2:
            return 1
        elif triangle == 3:
            return 0
        elif triangle == 4:
            return 0
    elif direction_idx == 3:
        if triangle == 1:
            return 1
        elif triangle == 2:
            return 0
        elif triangle == 3:
            return 2
        elif triangle == 4:
            return 1


def play_game(sy, sx, direction_idx):
    now_score = 0
    y, x = sy, sx
    while True:
        dy, dx = direction[direction_idx]
        ny, nx = y + dy, x + dx

        if oob(ny, nx) or area[ny][nx] == 5:
            y, x = ny, nx
            direction_idx = (direction_idx + 2) % 4
            now_score += 1
        elif area[ny][nx] >= 6:
            oy, ox = w_holes[area[ny][nx]][w_holes[area[ny][nx]].index((ny, nx)) ^ 1]
            y, x = oy, ox
        elif area[ny][nx] <= 0:
            y, x = ny, nx
        elif area[ny][nx] in (1, 2, 3, 4):
            y, x = ny, nx
            direction_idx = convert_direction(direction_idx, area[ny][nx])
            now_score += 1

        if not oob(y, x) and (area[y][x] == -1 or (y == sy and x == sx)):
            return now_score


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    w_holes = [None] * 6 + [[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if area[i][j] >= 6:
                w_holes[area[i][j]].append((i, j))

    max_answer = 0
    for i in range(n):
        for j in range(n):
            if not area[i][j]:
                for d_idx in range(4):
                    max_answer = max(max_answer, play_game(i, j, d_idx))

    print(f"#{test} {max_answer}")
