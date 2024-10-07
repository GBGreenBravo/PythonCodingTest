# 20241007
# 20:20
# 1 / 1

direction_dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

game_num = 0
while True:
    r, c = map(int, input().split())
    if not r + c:
        break

    area = [list(str(input())) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if area[i][j] == 'w':
                area[i][j] = '.'
                cy, cx = i, j
                break
            elif area[i][j] == 'W':
                area[i][j] = '+'
                cy, cx = i, j
                break
        else:
            continue
        break
    game_set = False

    moves = list(str(input()))
    for move in moves:
        if game_set:
            break

        dy, dx = direction_dict[move]
        ny, nx = cy + dy, cx + dx
        nny, nnx = cy + dy * 2, cx + dx * 2

        if area[ny][nx] in ('.', '+'):
            cy, cx = ny, nx
        elif area[ny][nx] == '#':
            pass
        elif area[ny][nx] == 'b':
            if area[nny][nnx] == '.':
                area[nny][nnx] = 'b'
                area[ny][nx] = '.'
                cy, cx = ny, nx
            elif area[nny][nnx] == '+':
                area[nny][nnx] = 'B'
                area[ny][nx] = '.'
                cy, cx = ny, nx
        elif area[ny][nx] == 'B':
            if area[nny][nnx] == '.':
                area[nny][nnx] = 'b'
                area[ny][nx] = '+'
                cy, cx = ny, nx
            elif area[nny][nnx] == '+':
                area[nny][nnx] = 'B'
                area[ny][nx] = '+'
                cy, cx = ny, nx

        game_set = not sum(map(lambda roww: roww.count('b'), area))

    game_num += 1
    print(f"Game {game_num}:", "complete" if game_set else "incomplete")
    if area[cy][cx] == '.':
        area[cy][cx] = 'w'
    elif area[cy][cx] == '+':
        area[cy][cx] = 'W'
    for row in area:
        print(*row, sep="")
