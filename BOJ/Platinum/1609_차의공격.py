# 20241229
# 1:55:13
# 1 / 6

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

row_sum = [sum(area[r]) for r in range(N)]
col_sum = [sum([area[r][c] for r in range(N)]) for c in range(N)]

row_sort1 = sorted([(v, i) for i, v in enumerate(row_sum)], reverse=True)
col_sort1 = sorted([(v, i) for i, v in enumerate(col_sum)], reverse=True)
row_sort2 = []
col_sort2 = []
for i in range(N - 1):
    for j in range(i + 1, N):
        row_sort2.append((row_sum[i] + row_sum[j], i, j))
        col_sort2.append((col_sum[i] + col_sum[j], i, j))
row_sort2.sort(reverse=True)
col_sort2.sort(reverse=True)

answer = 0
for r in range(N - 1):
    for rr in range(r + 1, N):
        m11, m12 = (-1, -1), (-1, -1)
        m21, m22 = (-1, -1), (-1, -1)
        for c in range(N):
            v1 = (col_sum[c] - area[r][c] - area[rr][c] * 2, c)
            if v1 > m11:
                m11, m12 = v1, m11
            elif v1 > m12:
                m12 = v1
            v2 = (col_sum[c] - area[r][c] * 2 - area[rr][c], c)
            if v2 > m21:
                m21, m22 = v2, m21
            elif v2 > m22:
                m22 = v2

        value = row_sum[r] + row_sum[rr]
        if m11[1] != m21[1]:
            answer = max(answer, value + m11[0] + m21[0])
        else:
            answer = max(answer, value + max(m11[0] + m22[0], m12[0] + m21[0]))
for r2_v, r, rr in row_sort2:
    for c1_v, c in col_sort1:
        value = r2_v + c1_v
        if value <= answer:
            break
        value -= area[r][c] * 2
        value -= area[rr][c] * 2
        answer = max(answer, value)
for r1_v, r in row_sort1:
    for c2_v, c, cc in col_sort2:
        value = r1_v + c2_v
        if value <= answer:
            break
        value -= area[r][c] * 2
        value -= area[r][cc] * 2
        answer = max(answer, value)
print(answer)
