# 20250109
# 34:32
# 1 / 1


def dfs(arr, cnt, row):
    global answer

    if cnt >= answer:
        return

    if row >= N:
        if not sum(arr[-1]):
            answer = cnt
        return

    for possible in possibles[sum(v << idx for idx, v in enumerate(arr[row - 1]))]:
        next_cnt = cnt
        next_arr = [a[:] for a in arr]
        for c in range(M):
            if possible & (1 << c):
                next_cnt += 1
                if c:
                    next_arr[row - 1][c - 1] ^= 1
                    next_arr[row][c - 1] ^= 1
                next_arr[row - 1][c] ^= 1
                next_arr[row][c] ^= 1
                if c != M - 1:
                    next_arr[row - 1][c + 1] ^= 1
                    next_arr[row][c + 1] ^= 1
                if row != N - 1:
                    if c:
                        next_arr[row + 1][c - 1] ^= 1
                    next_arr[row + 1][c] ^= 1
                    if c != M - 1:
                        next_arr[row + 1][c + 1] ^= 1

        dfs(next_arr, next_cnt, row + 1)


N, M = map(int, input().split())

possibles = [[] for _ in range(2 ** M)]
possibles[0].append(0)
for i in range(2 ** M):
    origin = [0] * M
    for j in range(M):
        if i & (1 << j):
            origin[j] = 1
    for j in range(2 ** M):
        now = [o for o in origin]
        for k in range(M):
            if j & (1 << k):
                if k:
                    now[k - 1] ^= 1
                now[k] ^= 1
                if k != M - 1:
                    now[k + 1] ^= 1

        if not sum(now):
            possibles[i].append(j)

area = [[int(i == '.') for i in str(input())] for _ in range(N)]

answer = N * M + 1
for i in range(2 ** M):
    now_area = [a[:] for a in area]
    clicked = 0
    for j in range(M):
        if i & (1 << j):
            clicked += 1
            now_area[0][j] ^= 1
            if j:
                now_area[0][j - 1] ^= 1
            if j != M - 1:
                now_area[0][j + 1] ^= 1
            if N != 1:
                now_area[1][j] ^= 1
                if j:
                    now_area[1][j - 1] ^= 1
                if j != M - 1:
                    now_area[1][j + 1] ^= 1

    dfs(now_area, clicked, 1)
print(-1 if answer == N * M + 1 else answer)
