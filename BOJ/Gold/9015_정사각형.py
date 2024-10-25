# 1 / 1
# 43:51
# 20241025

# 점의 개수가 최대 3000개 이므로, comb(3000, 2)는 4498500임.
# comb(N, 2)로 점 2개를 골라놓고,
# 두 점을 한 변으로 하는 정사각형 2개에 대해
# 유효한 정사각형이 하나라도 있으면, 최대값 갱신


def oob(yy, xx):
    return yy < 0 or 20001 < yy or xx < 0 or 20001 < xx


def cal_space(yy1, xx1, yy2, xx2):
    return (yy1 - yy2)**2 + (xx1 - xx2)**2


def cal_other_points(yy1, xx1, yy2, xx2):
    dy, dx = yy2 - yy1, xx2 - xx1
    return yy2 + dx, xx2 - dy, yy2 + dx - dy, xx2 - dy - dx


T = int(input())
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    exist_set = set()
    for i in range(N):
        r, c = points[i]
        points[i] = r + 10000, c + 10000
        exist_set.add((r + 10000) * 20001 + c + 10000)

    max_answer = 0
    for i in range(N - 1):
        y1, x1 = points[i]
        for j in range(i + 1, N):
            y2, x2 = points[j]

            space = cal_space(y1, x1, y2, x2)

            if space <= max_answer:
                continue

            oy1, ox1, oy2, ox2 = cal_other_points(y1, x1, y2, x2)
            if not (oob(oy1, ox1) or oob(oy2, ox2)):
                if oy1 * 20001 + ox1 in exist_set and oy2 * 20001 + ox2 in exist_set:
                    max_answer = space
                    break

            oy1, ox1, oy2, ox2 = cal_other_points(y2, x2, y1, x1)
            if not (oob(oy1, ox1) or oob(oy2, ox2)):
                if oy1 * 20001 + ox1 in exist_set and oy2 * 20001 + ox2 in exist_set:
                    max_answer = space
                    break

    print(max_answer)
