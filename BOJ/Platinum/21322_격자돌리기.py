# 20241125
# 18:16
# 1 / 1

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

order_area = [[-1] * N for _ in range(N)]
order_indexes = []
for i in range(N // 2):
    oi, oj = i, i
    index_arr = []
    order = 0
    for _ in range(N - (i * 2) - 1):
        index_arr.append((oi, oj))
        order_area[oi][oj] = [i, order]
        oi += 1
        order += 1
    for _ in range(N - (i * 2) - 1):
        index_arr.append((oi, oj))
        order_area[oi][oj] = [i, order]
        oj += 1
        order += 1
    for _ in range(N - (i * 2) - 1):
        index_arr.append((oi, oj))
        order_area[oi][oj] = [i, order]
        oi -= 1
        order += 1
    for _ in range(N - (i * 2) - 1):
        index_arr.append((oi, oj))
        order_area[oi][oj] = [i, order]
        oj -= 1
        order += 1
    order_indexes.append(index_arr)

rotated = [0] * (N // 2)
answers = []

for _ in range(M):
    aa, bb, cc = map(int, input().split())
    bb, cc = bb - 1, cc - 1

    if aa == 1:
        rotated[bb] += cc + 1
        rotated[bb] %= len(order_indexes[bb])
    elif aa == 2:
        y1, x1 = order_indexes[order_area[bb][cc][0]][(order_area[bb][cc][1] + rotated[order_area[bb][cc][0]]) % len(order_indexes[order_area[bb][cc][0]])]
        y2, x2 = order_indexes[order_area[bb][cc+1][0]][(order_area[bb][cc+1][1] + rotated[order_area[bb][cc+1][0]]) % len(order_indexes[order_area[bb][cc+1][0]])]
        y3, x3 = order_indexes[order_area[bb+1][cc][0]][(order_area[bb+1][cc][1] + rotated[order_area[bb+1][cc][0]]) % len(order_indexes[order_area[bb+1][cc][0]])]
        y4, x4 = order_indexes[order_area[bb+1][cc+1][0]][(order_area[bb+1][cc+1][1] + rotated[order_area[bb+1][cc+1][0]]) % len(order_indexes[order_area[bb+1][cc+1][0]])]
        area[y1][x1], area[y2][x2], area[y3][x3], area[y4][x4] = area[y3][x3], area[y1][x1], area[y4][x4], area[y2][x2]
    else:  # elif aa == 3:
        group_idx = order_area[bb][cc][0]
        y, x = order_indexes[group_idx][(order_area[bb][cc][1] + rotated[group_idx]) % len(order_indexes[group_idx])]
        answers.append(area[y][x])

print(*answers, sep="\n")
