# 20240930
# 23:13
# 1 / 1

t = int(input())
for test in range(1, t + 1):
    n, m, c = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    m_combs = [[True], [False]]
    for _ in range(m - 1):
        next_combs = []
        for now_comb in m_combs:
            next_combs.append(now_comb + [True])
            next_combs.append(now_comb + [False])
        m_combs = next_combs

    profits = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n + 1 - m):
            boxes = area[i][j:j + m]
            sum_boxes = sum(boxes)

            if sum_boxes <= c:
                profits[i][j] = sum([b**2 for b in boxes])
                continue

            ij_max = 0
            for now_comb in m_combs:
                ij_tmp = 0
                ij_sum = 0
                for idx in range(m):
                    if now_comb[idx]:
                        ij_tmp += boxes[idx]**2
                        ij_sum += boxes[idx]
                if ij_sum <= c:
                    ij_max = max(ij_max, ij_tmp)
            profits[i][j] = ij_max

    max_answer = 0
    for i in range(n):
        for j in range(n + 1 - m):
            y, x = i, j

            for ii in range(i, n):
                if ii == i:
                    for jj in range(j + m, n + 1 - m):
                        max_answer = max(max_answer, profits[i][j] + profits[ii][jj])
                else:
                    for jj in range(n + 1 - m):
                        max_answer = max(max_answer, profits[i][j] + profits[ii][jj])

    print(f"#{test} {max_answer}")
