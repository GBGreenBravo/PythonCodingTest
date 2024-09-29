# 20240929
# 16:50
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_dict = {'E': 0, 'W': 1, 'S': 2, 'N': 3}


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


n, m, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dead = [[0] * m for _ in range(n)]

score = 0
for _ in range(r):
    a_y, a_x, a_d = input().split()

    a_y, a_x = int(a_y) - 1, int(a_x) - 1
    dy, dx = direction[direction_dict[a_d]]

    if not dead[a_y][a_x]:
        dead[a_y][a_x] = 1
        tmp_score = 1

        y, x = a_y + dy, a_x + dx
        ey, ex = a_y + dy * area[a_y][a_x],  a_x + dx * area[a_y][a_x]
        while not oob(y, x) and not (y == ey and x == ex):
            if not dead[y][x]:
                dead[y][x] = 1
                tmp_score += 1

                if dy == 1:
                    ey = max(ey, y + area[y][x])
                elif dy == -1:
                    ey = min(ey, y - area[y][x])
                elif dx == 1:
                    ex = max(ex, x + area[y][x])
                elif dx == -1:
                    ex = min(ex, x - area[y][x])

            y, x = y + dy, x + dx

        score += tmp_score

    d_y, d_x = map(lambda inp: int(inp) - 1, input().split())
    dead[d_y][d_x] = 0

print(score)
for row in dead:
    print(*['F' if r else 'S' for r in row], sep=" ")
