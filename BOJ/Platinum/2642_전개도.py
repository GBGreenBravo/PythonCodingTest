# 20241028
# 46:30
# 1 / 1

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북 동 남 서
nesw = ((5, 1, 2, 4),
        (5, 3, 2, 0),
        (0, 1, 3, 4),
        (5, 4, 2, 1),
        (5, 0, 2, 3),
        (3, 1, 0, 4))
opposite_d_idx = (2, 3, 0, 1)


def oob(yy, xx):
    return yy < 0 or 6 <= yy or xx < 0 or 6 <= xx


area = [list(map(int, input().split())) for _ in range(6)]

possible = True
dice = [0] * 6
for i in range(6):
    for j in range(6):
        if area[i][j]:
            dice[0] = area[i][j]
            area[i][j] = 0

            queue = []

            for d_idx, (di, dj) in enumerate(direction):
                ni, nj = i + di, j + dj
                if oob(ni, nj) or not area[ni][nj]:
                    continue
                dice[nesw[0][d_idx]] = area[ni][nj]
                queue.append((ni, nj, nesw[0][d_idx], 0, opposite_d_idx[d_idx]))
                area[ni][nj] = 0

            while queue:
                y, x, face, before_face, enter_d_idx = queue.pop(0)
                start = nesw[face].index(before_face)
                for k in range(1, 4):
                    d_idx = (enter_d_idx + k) % 4
                    dy, dx = direction[d_idx]
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or not area[ny][nx]:
                        continue
                    next_face = nesw[face][(start + k) % 4]
                    if dice[next_face]:
                        possible = False
                        break
                    dice[next_face] = area[ny][nx]
                    queue.append((ny, nx, next_face, face, opposite_d_idx[d_idx]))
                    area[ny][nx] = 0
                else:
                    continue
                break

            break
    else:
        continue
    break

if 0 in dice:
    possible = False

if not possible:
    print(0)
else:
    for i in range(6):
        if dice[i] == 1:
            print(dice[(i + 3) % 6])
            break
