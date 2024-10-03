# 20241003
# 1 / 1
# 15:50

# 23288_주사위굴리기2

"""
풀이 시간: 16분 (10:36 ~ 11:52)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (10:36 - 10:39)
    이전 풀이방식 정확히 기억 나지는 않았습니다.
    끝나고 비교해보니,
    이전 풀이에서는 매번 굴릴 때마다, 그 칸의 점수를 계산하는 BFS했고
    이번 풀이에서는 칸별 점수가 바뀌지 않는 걸 인지하고, 초반에 BFS를 통해 그 값을 미리 다 계산해줬습니다.


2. 구현 (10:39 - 11:51)


3. 디버깅 (-)
"""

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def bfs():
    visited = [[0] * n for _ in range(n)]
    for sy in range(n):
        for sx in range(n):
            if not visited[sy][sx]:
                queue = deque()
                queue.append((sy, sx))

                groups = [(sy, sx)]

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or area[ny][nx] != area[sy][sx] or (ny, nx) in groups:
                            continue
                        queue.append((ny, nx))
                        groups.append((ny, nx))

                group_value = area[sy][sx] * len(groups)
                for gy, gx in groups:
                    visited[gy][gx] = group_value

    return visited


def roll(direction_idx):
    global dice

    bottom, top, east, west, north, south = dice
    if direction_idx == 0:
        dice = east, west, top, bottom, north, south
    elif direction_idx == 1:
        dice = south, north, east, west, bottom, top
    elif direction_idx == 2:
        dice = west, east, bottom, top, north, south
    elif direction_idx == 3:
        dice = north, south, east, west, top, bottom


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
score_area = bfs()

dice = 6, 1, 3, 4, 5, 2  # 밑/위/동/서/북/남
cy, cx = 0, 0
d_idx = 0

total_score = 0
for _ in range(m):
    roll(d_idx)

    cdy, cdx = direction[d_idx]
    cy, cx = cy + cdy, cx + cdx

    total_score += score_area[cy][cx]

    if area[cy][cx] < dice[0]:
        d_idx = (d_idx + 1) % 4
    elif area[cy][cx] > dice[0]:
        d_idx = (d_idx - 1) % 4

    cdy, cdx = direction[d_idx]
    ncy, ncx = cy + cdy, cx + cdx
    if oob(ncy, ncx):
        d_idx = (d_idx + 2) % 4

print(total_score)
