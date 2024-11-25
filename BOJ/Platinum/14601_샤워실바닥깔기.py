# 20241125
# 54:47
# 1 / 1

direction = ((1, 1), (1, -1), (-1, -1), (-1, 1))

K = int(input())
N = 2 ** K
ex, ey = map(lambda inp: int(inp) - 1, input().split())
ey = N - 1 - ey

area = [[0] * N for _ in range(N)]
flag = 0


def fill(sy, sx, length, d_idx):
    global flag

    if length == 1:
        flag += 1
        dy, dx = direction[d_idx]
        area[sy][sx], area[sy + dy][sx], area[sy][sx + dx] = flag, flag, flag
        return

    half = 2**length // 2

    if d_idx == 0:
        fill(sy, sx, length - 1, 0)
        fill(sy + half // 2, sx + half // 2, length - 1, 0)
        fill(sy, sx + half * 2 - 1, length - 1, 1)
        fill(sy + half * 2 - 1, sx, length - 1, 3)
    elif d_idx == 1:
        fill(sy, sx, length - 1, 1)
        fill(sy + half // 2, sx - half // 2, length - 1, 1)
        fill(sy, sx - half * 2 + 1, length - 1, 0)
        fill(sy + half * 2 - 1, sx, length - 1, 2)
    elif d_idx == 2:
        fill(sy, sx, length - 1, 2)
        fill(sy - half // 2, sx - half // 2, length - 1, 2)
        fill(sy - half * 2 + 1, sx, length - 1, 1)
        fill(sy, sx - half * 2 + 1, length - 1, 3)
    else:  # elif d_idx == 3:
        fill(sy, sx, length - 1, 3)
        fill(sy - half // 2, sx + half // 2, length - 1, 3)
        fill(sy - half * 2 + 1, sx, length - 1, 0)
        fill(sy, sx + half * 2 - 1, length - 1, 2)


def recur(sy, sx, length):
    global flag

    if length == 1:
        flag += 1
        area[sy][sx], area[sy][sx + 1], area[sy + 1][sx], area[sy + 1][sx + 1] = flag, flag, flag, flag
        return

    half = 2**length // 2

    if ey < sy + half and ex < sx + half:
        recur(sy, sx, length - 1)
        fill(sy, sx + half * 2 - 1, length - 1, 1)
        fill(sy + half * 2 - 1, sx, length - 1, 3)
        fill(sy + half * 2 - 1, sx + half * 2 - 1, length - 1, 2)
        fill(sy + half + half // 2 - 1, sx + half + half // 2 - 1, length - 1, 2)
    elif ey < sy + half and ex >= sx + half:
        recur(sy, sx + half, length - 1)
        fill(sy, sx, length - 1, 0)
        fill(sy + half * 2 - 1, sx, length - 1, 3)
        fill(sy + half + half // 2 - 1, sx + half // 2, length - 1, 3)
        fill(sy + half * 2 - 1, sx + half * 2 - 1, length - 1, 2)
    elif ey >= sy + half and ex < sx + half:
        recur(sy + half, sx, length - 1)
        fill(sy, sx, length - 1, 0)
        fill(sy + half // 2, sx + half + half // 2 - 1, length - 1, 1)
        fill(sy, sx + half * 2 - 1, length - 1, 1)
        fill(sy + half * 2 - 1, sx + half * 2 - 1, length - 1, 2)
    elif ey >= sy + half and ex >= sx + half:
        recur(sy + half, sx + half, length - 1)
        fill(sy, sx, length - 1, 0)
        fill(sy + half // 2, sx + half // 2, length - 1, 0)
        fill(sy, sx + half * 2 - 1, length - 1, 1)
        fill(sy + half * 2 - 1, sx, length - 1, 3)


recur(0, 0, K)

area[ey][ex] = -1
for row in area:
    print(*row, sep=" ")
