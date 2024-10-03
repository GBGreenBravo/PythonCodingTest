# 20241003
# 13:53
# 1 / 1

# 21608_상어초등학교

"""
풀이 시간: 14분 (18:18 ~ 18:32)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (18:18 - 18:22)
    이전 풀이방식에서는 인접선호학생수는 따로 변수로 관리했기에 코드가 좀 더 길었습니다.
    코드리뷰에서 다른 분들의 코드를 보고, 다 넣어놓고 sort()해도 시간복잡도 이슈가 없음을 알았기에,
    (시간복잡도 체크 후) 이번에는 모두 담아놓고 풀기로 했습니다.


2. 구현 (18:22 - 18:31)


3. 디버깅 (-)
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n = int(input())
area = [[0] * n for _ in range(n)]

favors = [None] + [None for _ in range(n**2)]
students_order = []
for _ in range(n**2):
    aa, bb, cc, dd, ee = map(int, input().split())
    favors[aa] = bb, cc, dd, ee
    students_order.append(aa)

for now_student in students_order:
    now_favors = favors[now_student]
    candidates = []

    for y in range(n):
        for x in range(n):
            if area[y][x]:
                continue
            favor_cnt = 0
            empty_cnt = 0
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx):
                    continue
                area_ny_nx = area[ny][nx]
                if not area_ny_nx:
                    empty_cnt += 1
                elif area[ny][nx] in now_favors:
                    favor_cnt += 1
            candidates.append((-favor_cnt, -empty_cnt, y, x))

    seat_y, seat_x = min(candidates)[2:]
    area[seat_y][seat_x] = now_student

answer = 0
for i in range(n):
    for j in range(n):
        near_favor_cnt = 0
        now_favors = favors[area[i][j]]
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if oob(ni, nj) or area[ni][nj] not in now_favors:
                continue
            near_favor_cnt += 1
        if near_favor_cnt:
            answer += 10**(near_favor_cnt - 1)
print(answer)
