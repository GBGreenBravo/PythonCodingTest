# 20240722
# 29:14

n, m = map(int, input().split())

board = []
answer = n * m

for i in range(n):
    board.append(list(str(input())))

for i in range(0, n - 7):
    for j in range(0, m - 7):
        criteria = board[i][j]
        cri = (i + j) % 2

        now = 0

        for a in range(0, 8):
            for b in range(0, 8):
                if (i + a + j + b) % 2 == cri:
                    if board[i + a][j + b] != criteria:
                        now += 1
                else:
                    if board[i + a][j + b] == criteria:
                        now += 1

        if min(now, 64-now) < answer:
            answer = min(now, 64-now)

print(answer)

# 두 인덱스의 합이 짝수인 곳이 같아야 하고, 홀수인 곳이 달라야 한다고 가정한다면
# 아래 코드와 같이, cri 쓸 필요 없어짐.
'''
n, m = map(int, input().split())

board = []
answer = n * m

for i in range(n):
    board.append(list(str(input())))

for i in range(0, n - 7):
    for j in range(0, m - 7):
        criteria = board[i][j]

        now = 0

        for a in range(0, 8):
            for b in range(0, 8):
                if (i + a + j + b) % 2 == 0:
                    if board[i + a][j + b] != criteria:
                        now += 1
                else:
                    if board[i + a][j + b] == criteria:
                        now += 1

        if min(now, 64-now) < answer:
            answer = min(now, 64-now)

print(answer)
'''