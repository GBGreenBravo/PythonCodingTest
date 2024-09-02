# 20240903
# 16:40
# 1 / 1

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def dfs(move_cnt, d, c1y, c1x, c2y, c2x):
    global answer

    dy, dx = direction[d]
    if not oob(c1y + dy, c1x + dx) and area[c1y + dy][c1x + dx] == '#':  # 벽으로 이동 못하면 가만히
        pass
    else:
        c1y, c1x = c1y + dy, c1x + dx
    if not oob(c2y + dy, c2x + dx) and area[c2y + dy][c2x + dx] == '#':
        pass
    else:
        c2y, c2x = c2y + dy, c2x + dx

    if oob(c1y, c1x) and oob(c2y, c2x):  # 둘다 나가면 return
        return
    if oob(c1y, c1x):  # 하나만 나가면 갱신
        answer = min(answer, move_cnt)
        return
    if oob(c2y, c2x):  # 하나만 나가면 갱신
        answer = min(answer, move_cnt)
        return
    else:  # 둘 다 안 나가면, 다음 방향으로 이동처리
        if move_cnt == 10:  # 이미 10번 이동했다면 return
            return
        for dd in range(4):
            dfs(move_cnt + 1, dd, c1y, c1x, c2y, c2x)


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# 코인2개 좌표 탐색
coin_1, coin_2 = None, None
for i in range(n):
    for j in range(m):
        if area[i][j] == 'o':
            area[i][j] = '.'
            if not coin_1:
                coin_1 = (i, j)
            else:
                coin_2 = (i, j)
    if coin_2:
        break

answer = 11  # 도달불가능한 초기값 11
# 상하좌우로 이동 dfs() 호출
dfs(1, 0, *coin_1, *coin_2)
dfs(1, 1, *coin_1, *coin_2)
dfs(1, 2, *coin_1, *coin_2)
dfs(1, 3, *coin_1, *coin_2)
print(answer if answer != 11 else -1)
