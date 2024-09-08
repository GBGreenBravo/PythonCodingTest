# 20240908
# 10:28
# 1 / 2

# BFS에서 visited 체크 제발 까먹지 말자...!!!

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


# 같은 섬의 칸들에 대해, 섬 번호로 바꾸는 함수
def differentiate(sy, sx, number):
    queue = deque()
    queue.append((sy, sx))

    area[sy][sx] = number

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and area[ny][nx] == 1:  # 섬 번호 2부터 시작하므로, visited 체크는 area[ny][nx] == 1로
                area[ny][nx] = number
                queue.append((ny, nx))


# 다른 섬 만날 때까지 BFS하면서, 최소 다리 길이를 반환하는 함수
def cal_bridge_length(sy, sx, island_number):
    queue = deque()
    queue.append((sy, sx, 0))

    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1

    while queue:
        y, x, distance = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx]:  # BFS에서 visited 체크 제발 까먹지 말자...!!!
                continue
            if not area[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx, distance + 1))
            elif area[ny][nx] != island_number:
                return distance

    return n**2  # 사방이 같은 섬으로 막혀있다면, 이 값 반환


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

# 섬 번호 2부터 시작해서, 각 섬의 칸마다 섬번호로 바꾸기
flag_number = 2
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            differentiate(i, j, flag_number)
            flag_number += 1

# 섬의 칸에 대해, 최소 다리 길이 계산
min_answer = n**2
for i in range(n):
    for j in range(n):
        if area[i][j]:
            min_answer = min(min_answer, cal_bridge_length(i, j, area[i][j]))
print(min_answer)
