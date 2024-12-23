# 20241224
# 1 / 8

# 비트마스킹이 항상 시간효율이 좋은 건 아님!


def change(arr, y, x):
    for dy, dx in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if ny < 0 or N <= ny or nx < 0 or N <= nx:
            continue
        arr[ny][nx] ^= 1


def check(first):
    global answer

    board = [a[:] for a in area]
    now_answer = 0
    for c in range(N):
        if first & 1 << c:
            change(board, 0, c)
            now_answer += 1
    for r in range(N - 1):
        for c in range(N):
            if board[r][c]:
                change(board, r + 1, c)
                now_answer += 1
    if sum(board[-1]):
        return
    answer = min(answer, now_answer)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
answer = N**2 + 1
for i in range(2**N):
    check(i)
print(answer if answer != N**2 + 1 else -1)
