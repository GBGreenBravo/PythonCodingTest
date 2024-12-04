# 20241204
# 3:13:42
# 1 / 8

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or R <= y or x < 0 or C <= x


def cal_connected_points(sy, sx):
    points = []
    now_value = area[sy * C + sx]
    for dy, dx in direction:
        ny, nx = sy + dy, sx + dx
        while True:
            if oob(ny, nx):
                break
            if area[ny * C + nx] != now_value:
                points.append((ny * C + nx))
                break
            ny, nx = ny + dy, nx + dx
    return points


R, C = map(int, input().split())
area = []
for _ in range(R):
    area.extend(list(str(input())))
text = str(input()) + "*"
len_text = len(text)

connected = []
for i in range(R):
    for j in range(C):
        connected.append(cal_connected_points(i, j))


def solve():
    visited = [[0] * (R * C) for _ in range(len_text + 1)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        finding, now, value = queue.popleft()

        if text[finding] == area[now]:
            if finding == len_text - 1:
                return value + 1
            if not visited[finding + 1][now]:
                visited[finding + 1][now] = 1
                queue.append((finding + 1, now, value + 1))
            continue

        for nex in connected[now]:
            if visited[finding][nex]:
                continue
            visited[finding][nex] = 1
            queue.append((finding, nex, value + 1))


answer = solve()
print(answer)
