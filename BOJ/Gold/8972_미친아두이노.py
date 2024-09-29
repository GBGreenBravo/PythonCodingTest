# 20240929
# 22:16
# 1 / 1

direction_jong = (None, (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1))
direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def move_arduinos():
    global game_set, area

    after_move = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if area[y][x]:
                nexts = []
                for dy, dx in direction_8:
                    ny, nx = y + dy, x + dx
                    nexts.append(abs(jy - ny) + abs(jx - nx))

                if not min(nexts):
                    game_set = True
                    return

                edy, edx = direction_8[nexts.index(min(nexts))]
                after_move[y + edy][x + edx] += 1

    for y in range(r):
        for x in range(c):
            if after_move[y][x] > 1:
                after_move[y][x] = 0

    area = after_move


r, c = map(int, input().split())
input_area = [list(str(input())) for _ in range(r)]
moves = list(str(input()))

area = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if input_area[i][j] == '.':
            pass
        elif input_area[i][j] == 'R':
            area[i][j] = 1
        elif input_area[i][j] == 'I':
            jy, jx = i, j

game_set = False
for idx, move in enumerate(moves):
    jdy, jdx = direction_jong[int(move)]
    jy, jx = jy + jdy, jx + jdx

    if area[jy][jx]:
        print("kraj", idx + 1)
        break

    move_arduinos()

    if game_set:
        print("kraj", idx + 1)
        break
else:
    for i in range(r):
        for j in range(c):
            if area[i][j]:
                area[i][j] = 'R'
                continue
            area[i][j] = '.'
    area[jy][jx] = 'I'

    for row in area:
        print(*row, sep="")
