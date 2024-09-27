# 20240927
# 11:20
# 1 / 2

# 14502_연구소

"""
풀이 시간: 12분 (17:07 - 17:22)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (17:07 - 17:11)
    (09/27 한정) 정독&메모 하지 않았습니다..
    문제 정독&메모 루틴의 소중함을 깨달은 하루였습니다.


2. 구현 (17:11 - 17:18)


3. 디버깅 (17:18 - 17:20)
"""



from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def check(y1, x1, y2, x2, y3, x3):
    copied_area = [row[:] for row in area]
    copied_area[y1][x1] = 1
    copied_area[y2][x2] = 1
    copied_area[y3][x3] = 1

    visited = [[0] * m for _ in range(n)]
    queue = deque()

    for fy, fx in fires:
        visited[fy][fx] = 1
        queue.append((fy, fx))

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or copied_area[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx))

    now_safe_cnt = 0
    for y in range(n):
        for x in range(m):
            if visited[y][x] or copied_area[y][x]:
                continue
            now_safe_cnt += 1

    global answer
    answer = max(answer, now_safe_cnt)


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

fires = []
for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            fires.append((i, j))

answer = 0

for i in range(n * m):
    iy, ix = divmod(i, m)
    if area[iy][ix]:
        continue
    for j in range(i + 1, n * m):
        jy, jx = divmod(j, m)
        if area[jy][jx]:
            continue
        for k in range(j + 1, n * m):
            ky, kx = divmod(k, m)
            if area[ky][kx]:
                continue

            check(iy, ix, jy, jx, ky, kx)

print(answer)
