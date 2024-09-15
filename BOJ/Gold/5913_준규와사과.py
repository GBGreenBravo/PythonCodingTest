# 20240915
# 08:54
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 5 <= y or x < 0 or 5 <= x


def dfs(y, x, cnt):
    if y + x == 8:
        if cnt == 25 - k:
            global answer
            answer += 1
        return
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or area[ny][nx]:
            continue
        area[ny][nx] = 1
        dfs(ny, nx, cnt + 1)
        area[ny][nx] = 0


area = [[0] * 5 for _ in range(5)]
k = int(input())
if k % 2:
    print(0)
else:
    for _ in range(k):
        yy, xx = map(lambda idx: int(idx) - 1, input().split())
        area[yy][xx] = 1
    area[0][0] = 1
    answer = 0
    dfs(0, 0, 1)
    print(answer)
