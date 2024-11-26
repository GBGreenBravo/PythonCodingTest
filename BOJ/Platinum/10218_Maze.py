# 20241126
# 13:56
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def check(sy, sx):
    y, x = sy, sx
    for d_idx in dfs_arr:
        dy, dx = direction[d_idx]
        while True:
            ny, nx = y + dy, x + dx
            if area[ny][nx] == 'O':
                return True
            elif area[ny][nx] == '#':
                break
            else:
                y, x = ny, nx

    return False


def dfs(cnt):
    global possible

    if possible:
        return

    if cnt == 10:
        for sy, sx in start_points:
            if not check(sy, sx):
                break
        else:
            possible = "".join([["R", "L", "D", "U"][d] for d in dfs_arr])
        return

    for d_idx in range(4):
        if dfs_arr and dfs_arr[-1] == d_idx:
            continue
        dfs_arr.append(d_idx)
        dfs(cnt + 1)
        dfs_arr.pop()


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    area = [list(str(input())) for _ in range(N)]

    start_points = []
    for i in range(N):
        for j in range(M):
            if area[i][j] == '.':
                start_points.append((i, j))

    possible = False
    dfs_arr = []
    dfs(0)
    print(possible if possible else "XHAE")
