# 20241125
# 1:05:54
# 1 / 6

N, M, K, t = map(int, input().split())
mold = set()
check = set()
for _ in range(M):
    aa, bb = map(lambda inp:int(inp) - 1, input().split())
    mold.add(aa * N + bb)
for _ in range(K):
    aa, bb = map(lambda inp:int(inp) - 1, input().split())
    check.add(aa * N + bb)

nexts = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for di, dj in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
            ni, nj = i + di, j + dj
            if not (ni < 0 or N <= ni or nj < 0 or N <= nj):
                nexts[i][j].append(ni * N + nj)

mold_b, mold_bb = set(), set()
in_a_row = 0
for tt in range(t):
    if tt < 3:
        next_mold = set()
        for now_mold in mold:
            my, mx = divmod(now_mold, N)
            next_mold.update(nexts[my][mx])
        mold, mold_b, mold_bb = next_mold, mold, mold_b
        continue

    next_mold = set(m for m in mold_bb)
    for now_mold in mold - mold_bb:
        my, mx = divmod(now_mold, N)
        next_mold.update(nexts[my][mx])
    if len(next_mold) == len(mold_bb):
        in_a_row += 1
        if in_a_row == 3:
            mold = [next_mold, mold_b, mold][(t - tt - 1) % 3]
            break
    else:
        in_a_row = 0
    mold, mold_b, mold_bb = next_mold, mold, mold_b

print("YES" if mold & check else "NO")
