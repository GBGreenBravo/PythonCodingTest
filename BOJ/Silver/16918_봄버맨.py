# 20240731
# 15:20

r, c, n = map(int, input().split())
board = [list(str(input())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        board[i][j] = 2 if board[i][j] == 'O' else 0


def install_bombs():
    for y in range(r):
        for x in range(c):
            if board[y][x] == 0:
                board[y][x] = 2  # 1초 뒤의 값을 미리 계산하여, 3이 아닌 2로 넣어줌.
            else:
                board[y][x] -= 1  # 다음에 터질 폭탄은 1이 됨.


def explode():
    exploding_lst = []
    for y in range(r):
        for x in range(c):
            if board[y][x] == 1:
                exploding_lst.append((y, x))

    exploding_set = set()
    for exploding in exploding_lst:
        y, x = exploding
        exploding_set.add(exploding)
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c:
                exploding_set.add((ny, nx))

    for exploding in exploding_set:
        board[exploding[0]][exploding[1]] = 0


sec = 1
while sec != n:
    sec += 1
    if sec % 2 == 0:
        install_bombs()
    else:
        explode()

for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            print(".", end="")
        else:
            print("O", end="")
    print()


# explode() 함수에서, set으로 다시 계산하지 않고, 터지는 폭탄 주변에 곧 터질 폭탄(1 값을 가진 곳)은 스킵을 시켜주고 폭발시키면 됨.
# 이렇게 하면 시간, 메모리 모두 감소되는 아래의 코드 나옴.
"""
r, c, n = map(int, input().split())
board = [list(str(input())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        board[i][j] = 2 if board[i][j] == 'O' else 0


def install_bombs():
    for y in range(r):
        for x in range(c):
            if board[y][x] == 0:
                board[y][x] = 2
            else:
                board[y][x] -= 1


def explode():
    for y in range(r):
        for x in range(c):
            if board[y][x] == 1:
                board[y][x] = 0
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 1:
                        board[ny][nx] = 0


sec = 1
while sec != n:
    sec += 1
    if sec % 2 == 0:
        install_bombs()
    else:
        explode()

for i in range(r):
    print(*['.' if board[i][j] == 0 else 'O' for j in range(c)], sep="")
"""