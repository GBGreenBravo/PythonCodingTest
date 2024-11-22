# 20241122
# 20:22
# 1 / 3

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


N, M = map(int, input().split())
area = [['#'] * (M + 2)] + [['#'] + list(str(input())) + ['#'] for _ in range(N)] + [['#'] * (M + 2)]

red_y, red_x, blue_y, blue_x = None, None, None, None
for i in range(N + 2):
    for j in range(M + 2):
        if area[i][j] == 'R':
            red_y, red_x = i, j
            area[i][j] = '.'
        elif area[i][j] == 'B':
            blue_y, blue_x = i, j
            area[i][j] = '.'


def dfs(cnt, d_idx, ry, rx, by, bx):
    global answer

    if answer:
        return

    if cnt == 10:
        return

    red_out, blue_out = False, False

    dy, dx = direction[d_idx]

    ory, orx = ry, rx
    while True:
        nry, nrx = ry + dy, rx + dx
        if area[nry][nrx] == '#':
            break
        elif area[nry][nrx] == '.':
            ry, rx = nry, nrx
        elif area[nry][nrx] == 'O':
            red_out = True
            break

    oby, obx = by, bx
    while True:
        nby, nbx = by + dy, bx + dx
        if area[nby][nbx] == '#':
            break
        elif area[nby][nbx] == '.':
            by, bx = nby, nbx
        elif area[nby][nbx] == 'O':
            blue_out = True
            break

    if blue_out:
        return
    if red_out:
        answer = 1
        return

    if (ry, rx) == (by, bx):
        if abs(ry - ory) + abs(rx - orx) < abs(by - oby) + abs(bx - obx):
            by, bx = by - dy, bx - dx
        else:
            ry, rx = ry - dy, rx - dx

    for n_d_idx in range(4):
        if d_idx != n_d_idx:
            dfs(cnt + 1, n_d_idx, ry, rx, by, bx)


answer = 0
for i in range(4):
    dfs(0, i, red_y, red_x, blue_y, blue_x)
print(answer)
