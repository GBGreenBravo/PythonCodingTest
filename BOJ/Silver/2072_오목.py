# 20240930
# 10:31
# 1 / 1

direction = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def oob(y, x):
    return y < 0 or 19 <= y or x < 0 or 19 <= x


def check(sy, sx):
    in_a_rows = []
    criteria = area[sy][sx]

    for di, (dy, dx) in enumerate(direction[:4]):
        in_a_row = 1

        y, x = sy + dy, sx + dx
        while not oob(y, x) and area[y][x] == criteria:
            y, x = y + dy, x + dx
            in_a_row += 1

        by, bx = direction[di + 4]
        y, x = sy + by, sx + bx
        while not oob(y, x) and area[y][x] == criteria:
            y, x = y + by, x + bx
            in_a_row += 1

        in_a_rows.append(in_a_row)

    return 5 in in_a_rows


area = [[0] * 19 for _ in range(19)]

n = int(input())
input_infos = [None] + [tuple(map(lambda inp: int(inp) - 1, input().split())) for _ in range(n)]
for idx in range(1, n + 1):
    i, j = input_infos[idx]

    area[i][j] = idx % 2 + 1

    if check(i, j):
        print(idx)
        break
else:
    print(-1)
