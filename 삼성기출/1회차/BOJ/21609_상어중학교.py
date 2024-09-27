# 20240913
# 1:01:00
# 1 / 2

"""
풀이 시간: 1시간 1분 (14:10 ~ 15:11)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (14:10 - 14:19)


2. 구현 (14:19 - 14:52)


3. 검증 (14:52 - 15:05)


4. 틀렸습니다 (15:05 - 15:11)

"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def find_biggest():
    max_group = []
    max_rainbow_cnt = 0

    visited = [[0] * n for _ in range(n)]

    group_flag = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > 0:
                group_flag += 1
                visited[i][j] = group_flag
                criteria = area[i][j]

                queue = deque()
                queue.append((i, j))

                now_group = [(i, j)]
                now_rainbow_cnt = 0

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] == group_flag or area[ny][nx] not in [criteria, 0]:
                            continue
                        visited[ny][nx] = group_flag
                        queue.append((ny, nx))
                        now_group.append((ny, nx))
                        if area[ny][nx] == 0:
                            now_rainbow_cnt += 1

                if len(now_group) > len(max_group):
                    max_group = now_group
                    max_rainbow_cnt = now_rainbow_cnt
                elif len(now_group) == len(max_group):
                    if now_rainbow_cnt > max_rainbow_cnt:
                        max_group = now_group
                        max_rainbow_cnt = now_rainbow_cnt
                    elif now_rainbow_cnt == max_rainbow_cnt:
                        c_now = [k for k in now_group if area[k[0]][k[1]]]
                        c_max = [k for k in max_group if area[k[0]][k[1]]]

                        if c_now[0] > c_max[0]:
                            max_group = now_group
                            max_rainbow_cnt = now_rainbow_cnt

    return max_group


def rotate_counterclockwise():
    global area
    area = [list(row) for row in list(zip(*area))[::-1]]


def gravity():
    global area
    copied_area = [row[:] for row in area]
    copied_area = [list(row[::-1]) for row in zip(*copied_area)]

    for r in range(n):
        new_row = []
        tmp = []
        for c in range(n - 1, -1, -1):
            col = copied_area[r][c]
            if col == -2:
                tmp.insert(0, -2)
            elif col == -1:
                tmp.append(-1)
                new_row.extend(tmp)
                tmp = []
            else:
                tmp.append(col)
        new_row.extend(tmp)
        copied_area[r] = new_row[::-1]

    copied_area = [list(row) for row in list(zip(*copied_area))[::-1]]
    area = copied_area


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

score = 0

while True:
    biggest = find_biggest()
    if len(biggest) < 2:
        break

    for my, mx in biggest:
        area[my][mx] = -2

    score += len(biggest) ** 2
    gravity()
    rotate_counterclockwise()
    gravity()

print(score)
