# 20240726
# 14:20

board = [list(str(input())) for _ in range(10)]


def oob(yy, xx):
    return not(0 <= yy < 10) or not(0 <= xx < 10)


def check(y, x):
    for dy, dx in ((1, 0), (1, 1), (0, 1), (-1, 1)):
        empty, goo = 0, 0
        for i in range(5):
            ny, nx = y + dy * i, x + dx * i
            if oob(ny, nx) or board[ny][nx] == 'O':
                break
            if board[ny][nx] == '.':
                empty += 1
            elif board[ny][nx] == 'X':
                goo += 1
        else:
            if empty == 1 and goo == 4:
                return True
    return False


for i in range(10):
    for j in range(10):
        if check(i, j):
            print(1)
            break
    else:
        continue
    break
else:
    print(0)
