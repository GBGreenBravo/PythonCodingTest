# 20240922
# 23;57
# 1 / 1


def operate(k_num, sy, sx, length):
    new_area = [area[row][sx:sx + length] for row in range(sy, sy + length)]

    if k_num == 1:    # 상하 반전
        new_area = new_area[::-1]
    elif k_num == 2:  # 좌우 반전
        new_area = [row[::-1] for row in new_area]
    elif k_num == 3:  # 시계방향 90도 회전
        new_area = [list(row)[::-1] for row in zip(*new_area)]
    elif k_num == 4:  # 반시계방향 90도 회전
        new_area = [list(row) for row in reversed(list(zip(*new_area)))]

    for y in range(length):
        for x in range(length):
            area[sy + y][sx + x] = new_area[y][x]


n, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2**n)]
commands = [tuple(map(int, input().split())) for _ in range(r)]

for k, l in commands:
    # 1~4 단계
    if k <= 4:
        for i in range(0, 2**n, 2**l):
            for j in range(0, 2**n, 2**l):
                operate(k, i, j, 2**l)

    # 5~8 단계
    else:
        # 배열 압축
        compressed = []
        for i in range(0, 2**n, 2**l):
            c_row = []
            for j in range(0, 2**n, 2**l):
                c_row.append([area[row][j:j + 2**l] for row in range(i, i + 2**l)])
            compressed.append(c_row)
        area = compressed

        # 배열 연산 수행 (k-4 연산을, 압축된 배열 전체에 대해 수행하는 것과 같음)
        operate(k - 4, 0, 0, 2**(n - l))

        # 배열 확장
        expanded = [[0] * (2**n) for _ in range(2**n)]
        for ii in range(2**(n - l)):
            for jj in range(2**(n - l)):
                box_area = area[ii][jj]
                si, sj = ii * 2**l, jj * 2**l
                for i in range(2**l):
                    for j in range(2**l):
                        expanded[si + i][sj + j] = box_area[i][j]
        area = expanded

for rr in area:
    print(*rr, sep=" ")


# 5~8단계에 대해, 배열 압축/확장 하지 않고,
# 전체에 대해 k연산 적용한 후, 각 2**l * 2**l 배열에 대해 보완 연산 적용시키는 코드
"""
def operate(k_num, sy, sx, length):
    new_area = [area[row][sx:sx + length] for row in range(sy, sy + length)]

    if k_num == 1:    # 상하 반전
        new_area = new_area[::-1]
    elif k_num == 2:  # 좌우 반전
        new_area = [row[::-1] for row in new_area]
    elif k_num == 3:  # 시계방향 90도 회전
        new_area = [list(row)[::-1] for row in zip(*new_area)]
    elif k_num == 4:  # 반시계방향 90도 회전
        new_area = [list(row) for row in reversed(list(zip(*new_area)))]

    for y in range(length):
        for x in range(length):
            area[sy + y][sx + x] = new_area[y][x]


n, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2**n)]
commands = [tuple(map(int, input().split())) for _ in range(r)]

for k, l in commands:
    # 1~4 단계
    if k <= 4:
        for i in range(0, 2**n, 2**l):
            for j in range(0, 2**n, 2**l):
                operate(k, i, j, 2**l)

    # 5~8 단계
    else:
        # 배열 전체에 k - 4 연산 수행
        operate(k - 4, 0, 0, 2**n)

        # 각 2**l * 2**l 배열에 대해, 위 연산을 복구
        for i in range(0, 2 ** n, 2 ** l):
            for j in range(0, 2 ** n, 2 ** l):
                # 5->5 / 6->6 / 7->8 / 8->7
                operate(k - 4 if k <= 6 else k+1 - 4 if k % 2 else k-1 - 4, i, j, 2**l)

for rr in area:
    print(*rr, sep=" ")
"""