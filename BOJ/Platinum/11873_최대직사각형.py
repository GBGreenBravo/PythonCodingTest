# 20241028
# 27:51
# 1 / 1

while True:
    N, M = map(int, input().split())
    if not N + M:
        break

    area = [list(map(int, input().split())) for _ in range(N)]

    # 왼쪽에 연속되는 1의 누적합 배열
    left = [[0] * M for _ in range(N)]
    for i in range(N):
        j = 0
        in_a_row = 0
        while j < M:
            if area[i][j]:
                in_a_row += 1
                left[i][j] = in_a_row
            else:
                in_a_row = 0
            j += 1

    # 위쪽에 연속되는 1의 누적합 배열
    up = [[0] * M for _ in range(N)]
    for i in range(M):
        j = 0
        in_a_row = 0
        while j < N:
            if area[j][i]:
                in_a_row += 1
                up[j][i] = in_a_row
            else:
                in_a_row = 0
            j += 1

    max_answer = 0
    # 왼쪽/위쪽의 연속 1 계산했으므로, 배열 우하단부터 탐색하는 것이 효율적임.
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if area[i][j]:  # 현재 (i, j)가 1이라면, 최대값 갱신 가능
                up_max = up[i][j]
                left_max = left[i][j]
                if up_max * left_max <= max_answer:  # (왼쪽 누적 최대 * 위쪽 누적 최대)가 이미 최대값 이하면, 갱신 가능성 없으므로 continue
                    continue

                # (i, j)에서 j 하나씩 줄이며, 최대값 갱신
                up_now = up[i][j]
                for width in range(1, left_max + 1):
                    up_now = min(up_now, up[i][j + 1 - width])
                    if up_now * width > max_answer:
                        max_answer = up_now * width
                    elif up_now * left_max <= max_answer:  # (최소 높이 * 최대 너비)가 최대값 이하 되면, break
                        break

                # (i, j)에서 i 하나씩 줄이며, 최대값 갱신
                left_now = left[i][j]
                for height in range(1, up_max + 1):
                    left_now = min(left_now, left[i + 1 - height][j])
                    if left_now * height > max_answer:
                        max_answer = left_now * height
                    elif left_max * height <= max_answer:  # (최소 너비 * 최대 높이)가 최대값 이하 되면, break
                        break
    print(max_answer)
