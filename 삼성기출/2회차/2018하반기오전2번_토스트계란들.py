# 20240930
# 18:44
# 1 / 2

# 16234_인구이동

"""
풀이 시간: 19분 (14:29 - 14:47)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (14:29 - 14:32)


2. 구현 (14:32 - 14:41)
    이전 풀이와 구현 방식이 거의 다 같습니다.
    이전 풀이 시점부터 BFS는 스타일이 확고히 굳어진 것 같습니다.


3. 디버깅 (-)


4. 틀렸습니다 (14:43 - 14:47)
    문제를 다시 읽고 문제 오해는 아니라고 판단했고,
    코드를 하나씩 정독하는 과정에서 발견했습니다.

    connected[ny][nx].append((y, x))로 적어야 할 부분에,
    connected[ny][nx].append((ny, x))로 적어서 틀렸습니다.
"""

from collections import deque

direction = (0, 1), (1, 0),


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def open_border():
    global border_opened

    for y in range(n):
        for x in range(n):
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if not oob(ny, nx) and (l <= abs(area[y][x] - area[ny][nx]) <= r):
                    border_opened = True
                    connected[y][x].append((ny, nx))
                    connected[ny][nx].append((y, x))


def merge_and_distribute():
    visited = [[0] * n for _ in range(n)]
    for sy in range(n):
        for sx in range(n):
            if not visited[sy][sx]:
                group_indexes = [(sy, sx)]
                group_value = area[sy][sx]

                visited[sy][sx] = 1

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for ny, nx in connected[y][x]:
                        if visited[ny][nx]:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_indexes.append((ny, nx))
                        group_value += area[ny][nx]

                if len(group_indexes) == 1:
                    continue

                distributed_value = group_value // len(group_indexes)

                for gy, gx in group_indexes:
                    area[gy][gx] = distributed_value


n, l, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

answer = 0

connected = [[[] for _ in range(n)] for _ in range(n)]
border_opened = False
open_border()

while border_opened:
    answer += 1

    merge_and_distribute()

    connected = [[[] for _ in range(n)] for _ in range(n)]
    border_opened = False
    open_border()
print(answer)
