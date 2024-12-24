# 20241224
# 1 / 1


def change(arr, y, x):
    for dy, dx in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if ny < 0 or M <= ny or nx < 0 or N <= nx:
            continue
        arr[ny][nx] ^= 1


def check(first):
    global answer

    board = [a[:] for a in area]
    now_answer = []
    for c in range(N):
        if first & 1 << c:
            change(board, 0, c)
            now_answer.append((0, c))
    for r in range(M - 1):
        for c in range(N):
            if board[r][c]:
                change(board, r + 1, c)
                now_answer.append((r + 1, c))
    if sum(board[-1]) or len(now_answer) > answer[0]:
        return
    elif len(now_answer) == answer[0]:
        answer[1] = max(answer[1], now_answer)
    else:
        answer = [len(now_answer), now_answer]


M, N = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(M)]
answer = [M * N + 1, []]
for i in range(2**N):
    check(i)
if answer[0] == M * N + 1:
    print("IMPOSSIBLE")
else:
    p_arr = [[0] * N for _ in range(M)]
    for ay, ax in answer[1]:
        p_arr[ay][ax] = 1
    for p_row in p_arr:
        print(*p_row)
