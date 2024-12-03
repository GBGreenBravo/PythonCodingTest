# 20241203
# 15:12
# 1 / 1


def possible(y, x, num):
    if num in area[y]:
        return False
    if num in [area[r][x] for r in range(9)]:
        return False
    yy, xx = y // 3 * 3, x // 3 * 3
    if num in [area[yy][xx], area[yy][xx + 1], area[yy][xx + 2],
               area[yy + 1][xx], area[yy + 1][xx + 1], area[yy + 1][xx + 2],
               area[yy + 2][xx], area[yy + 2][xx + 1], area[yy + 2][xx + 2]]:
        return False
    return True


def check(cnt):
    if cnt == total:
        for row in area:
            print(*row, sep="")
        exit()

    y, x = zeros[cnt]
    for num in range(1, 10):
        if possible(y, x, num):
            area[y][x] = num
            check(cnt + 1)
            area[y][x] = 0


area = [[int(i) for i in str(input())] for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        if not area[i][j]:
            zeros.append((i, j))
total = len(zeros)
check(0)
