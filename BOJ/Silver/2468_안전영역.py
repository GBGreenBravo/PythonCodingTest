# 20230724
# 40:42

from copy import deepcopy
from collections import deque


def check_secure_area(arr, nn):
    gone = [[0] * nn for _ in range(nn)]
    for i in range(nn):
        for j in range(nn):
            if arr[i][j] == 0:
                gone[i][j] = 1

    secure_area_cnt = 0
    for i in range(nn):
        for j in range(nn):
            if gone[i][j] == 1:
                continue
            else:
                secure_area_cnt += 1
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.pop()
                    gone[y][x] = 1
                    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < nn and 0 <= nx < nn and gone[ny][nx] == 0:
                            queue.append((ny, nx))
    return secure_area_cnt


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

mx = 1
for rain in range(1, max([max(i) for i in area])):
    area_copy = deepcopy(area)
    for i in range(n):
        for j in range(n):
            if area[i][j] - rain <= 0:
                area_copy[i][j] = 0

    mx = max(mx, check_secure_area(area_copy, n))

print(mx)


# area_copy 활용하지 말고 바로 gone 활용해도 됨.
# bfs 형식을 더 다듬자.
"""
from collections import deque


def check_secure_area():
    secure_area_cnt = 0
    for i in range(n):
        for j in range(n):
            if gone[i][j] == 1:
                continue
            else:
                secure_area_cnt += 1
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.pop()
                    gone[y][x] = 1
                    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n and gone[ny][nx] == 0:
                            queue.append((ny, nx))
    return secure_area_cnt


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

mx = 1
for rain in range(1, max([max(i) for i in area])):
    gone = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] - rain <= 0:
                gone[i][j] = 1
    mx = max(mx, check_secure_area())

print(mx)
"""