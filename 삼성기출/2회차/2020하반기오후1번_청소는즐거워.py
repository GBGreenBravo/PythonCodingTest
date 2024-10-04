# 20241003
# 25:33
# 1 / 1

# 20057_마법사상어와토네이도

"""
풀이 시간: 26분 (16:40 ~ 17:06)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:40 - 16:43)


2. 구현 (16:43 - 17:05)
    이전 풀이에서는 왼쪽방향으로 cleaning_d를 고정해두고, 좌표기준으로 매번 돌려서 활용했지만,
    이번 풀이에서는 우/하/좌/상 에 대한 모든 (dy,dx,percentage)를 하드코딩 했습니다.
    (주석처리된 코드로, 한 방향만 하드코딩하고 별도의 반복문으로 출력값 그대로 복붙)


3. 디버깅 (-)
"""

cleaning_d = [[(2, 0, 0.02), (1, 1, 0.1), (1, 0, 0.07), (1, -1, 0.01), (0, 2, 0.05), (-1, 1, 0.1), (-1, 0, 0.07), (-1, -1, 0.01), (-2, 0, 0.02)], [(0, -2, 0.02), (1, -1, 0.1), (0, -1, 0.07), (-1, -1, 0.01), (2, 0, 0.05), (1, 1, 0.1), (0, 1, 0.07), (-1, 1, 0.01), (0, 2, 0.02)], ((-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)), [(0, 2, 0.02), (-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01), (-2, 0, 0.05), (-1, -1, 0.1), (0, -1, 0.07), (1, -1, 0.01), (0, -2, 0.02)]]
# new_cleaning_d = [((-2, 0, 0.02),
#               (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
#               (0, -2, 0.05),  # (0, -1)은 따로 처리!
#               (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01),
#               (2, 0, 0.02))]
# for _ in range(3):
#     print(_ + 1)
#     new_dd = []
#     for dy, dx, percentage in new_cleaning_d[-1]:
#         new_dd.append((dx, -dy, percentage))
#     new_cleaning_d.append(new_dd)
#
# new_cleaning_d[0], new_cleaning_d[1], new_cleaning_d[2], new_cleaning_d[3] = new_cleaning_d[2], new_cleaning_d[3], new_cleaning_d[0], new_cleaning_d[1]
# print(new_cleaning_d)

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

spiral_visited = [[0] * n for _ in range(n)]
spiral_visited[0][0] = 1
i, j, ij_d = 0, 0, 0
routes = [(0, 0)]
while not (i == n // 2 and j == n // 2):
    di, dj = direction[ij_d]
    ni, nj = i + di, j + dj
    if oob(ni, nj) or spiral_visited[ni][nj]:
        ij_d = (ij_d + 1) % 4
        di, dj = direction[ij_d]
        ni, nj = i + di, j + dj
    spiral_visited[ni][nj] = 1
    routes.append((ni, nj))
    i, j = ni, nj
routes.reverse()

oob_dust = 0
for i in range(n**2 - 1):
    prev_y, prev_x = routes[i]
    curr_y, curr_x = routes[i + 1]

    now_d_idx = direction.index((curr_y - prev_y, curr_x - prev_x))

    now_dust_sum, now_remain_dust = area[curr_y][curr_x], area[curr_y][curr_x]
    area[curr_y][curr_x] = 0

    for dy, dx, percentage in cleaning_d[now_d_idx]:
        ny, nx = curr_y + dy, curr_x + dx
        spreading_dust = int(now_dust_sum * percentage)
        now_remain_dust -= spreading_dust
        if oob(ny, nx):
            oob_dust += spreading_dust
        else:
            area[ny][nx] += spreading_dust

    more_y, more_x = curr_y + direction[now_d_idx][0], curr_x + direction[now_d_idx][1]
    if oob(more_y, more_x):
        oob_dust += now_remain_dust
    else:
        area[more_y][more_x] += now_remain_dust

print(oob_dust)
