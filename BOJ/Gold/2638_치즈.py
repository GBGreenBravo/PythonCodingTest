# 20240818
# 14:21
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def spread_2(sy, sx):  # 해당 좌표를 외부 공기(2)로 바꾸고 접하는 0을 모두 2로 전파시키는 함수
    area[sy][sx] = 2

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] != 0:
                continue
            area[ny][nx] = 2
            queue.append((ny, nx))


def check_soon_melted(y, x):  # 해당 좌표의 상하좌우를 탐색하고 외부공기와 2면 이상이 접하는지 체크하는 함수
    near_2 = 4
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            near_2 -= 1
            continue
        if area[ny][nx] == 0 or area[ny][nx] == 1:
            near_2 -= 1

    return True if near_2 >= 2 else False


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# 테두리 좌표에 존재하는 0을 모두 2로 전파시키기. (외부 공기(2)와 내부 공기(0)의 구분을 위함)
for i in range(n):
    if area[i][0] == 0:
        spread_2(i, 0)
    if area[i][m - 1] == 0:
        spread_2(i, m - 1)
for i in range(1, m - 1):
    if area[0][i] == 0:
        spread_2(0, i)
    if area[n - 1][i] == 0:
        spread_2(n - 1, i)

one_indexes = []  # 치즈 위치한 좌표 저장
for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            one_indexes.append((i, j))

time = 0
while one_indexes:
    time += 1
    soon_melted = []  # 이번 time에 사라질 치즈들 저장

    for oy, ox in one_indexes:
        if check_soon_melted(oy, ox):
            soon_melted.append((oy, ox))

    for melted in soon_melted:  # 사라질 치즈에 대해, 2 전파시키고 제거
        spread_2(*melted)
        one_indexes.remove(melted)

print(time)
