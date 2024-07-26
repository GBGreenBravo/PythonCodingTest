# 20240726
# 29:25

king, stone, n = map(str, input().split())
moves = [str(input()) for _ in range(int(n))]

board = [[0] * 8 for _ in range(8)]
row = ['8', '7', '6', '5', '4', '3', '2', '1']
col = ["A", "B", "C", "D", "E", "F", "G", "H"]

king, stone = [row.index(king[1]), col.index(king[0])], [row.index(stone[1]), col.index(stone[0])]
board[king[0]][king[1]] = 'k'
board[stone[0]][stone[1]] = 's'

move_decode = {"R": (0, 1), "L": (0, -1), "B": (1, 0), "T": (-1, 0), "RT": (-1, 1), "LT": (-1, -1), "RB": (1, 1), "LB": (1, -1)}
moves = [move_decode[move] for move in moves]


def move_king(king1, moving):
    y, x = king1
    dy, dx = moving

    ny, nx = y + dy, x + dx
    if not(0 <= ny < 8) or not(0 <= nx < 8):
        return [y, x]
    if board[ny][nx] == 0:
        board[y][x] = 0
        board[ny][nx] = 'k'
        return [ny, nx]
    else:  # 돌 있는 경우
        if 0 <= ny + dy < 8 and 0 <= nx + dx < 8:
            board[ny + dy][nx + dx] = 's'
            board[ny][nx] = 'k'
            board[y][x] = 0
            return [ny, nx]
    return [y, x]


for move in moves:
    king = move_king(king, move)

last_king = col[king[1]] + row[king[0]]
last_stone = "LAST_STONE"
for i in range(8):
    for j in range(8):
        if board[i][j] == 's':
            last_stone = col[j] + row[i]

print(last_king)
print(last_stone)
