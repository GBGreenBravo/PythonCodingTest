# 20241221
# 1 / 1

direction = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 10 <= y or x < 0 or 10 <= x


area = [[int(i == 'O') for i in str(input())] for _ in range(10)]

candidates = [[0, area]]
for comb in range(2**10):
    tmp = [a[:] for a in area]
    cnt = 0
    for c in range(10):
        if comb & 1:
            cnt += 1
            for di, dj in direction:
                ni, nj = di, c + dj
                if not oob(ni, nj):
                    tmp[ni][nj] ^= 1
        comb >>= 1
    candidates.append([cnt, tmp])

answer = 101
for r in range(1, 10):
    for i in range(len(candidates)):
        cnt, now = candidates[i]
        for c in range(10):
            if now[r - 1][c]:
                cnt += 1
                for di, dj in direction:
                    ni, nj = r + di, c + dj
                    if not oob(ni, nj):
                        now[ni][nj] ^= 1
        candidates[i][0] = cnt
        if r == 9:
            if not sum(now[-1]):
                answer = min(answer, cnt)

print(-1 if answer == 101 else answer)
