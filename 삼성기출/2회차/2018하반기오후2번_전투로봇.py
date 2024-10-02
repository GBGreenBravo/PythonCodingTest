# 20241001
# 15:09
# 1 / 1

# 16236_아기상어

"""
풀이 시간: 15분 (14:15 - 14:20)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:15 - 14:20)
    백준의 아기상어 문제보다 지문이 친절했기에, 그대로 구현해주면 됐습니다.


2. 구현 (14:20 - 14:28)
    이전 풀이보다, 함수 안에서 과도하게 많은 일을 하기보다, 메인 코드에서 로직을 더욱 쉽게 확인할 수 있게 구현했습니다.
    그리고, 스텝 기반 BFS를 채택하였다는 차이와 sort()를 하지 않고 값 하나만 쓸 거니까 (코드리뷰에서 알게 된) min()으로 값을 가져왔다는 차이가 있습니다.


3. 디버깅 (-)
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def find_next_monster():
    visited = [[0] * n for _ in range(n)]
    visited[ry][rx] = 1

    queue = deque()
    queue.append((ry, rx))

    distance = 0
    while queue:
        distance += 1

        next_queue = deque()
        edibles = []

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx] > size:
                    continue
                if area[ny][nx] and area[ny][nx] < size:
                    edibles.append((ny, nx))
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))

        if edibles:
            return distance, *min(edibles)

        queue = next_queue


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            area[i][j] = 0
            ry, rx = i, j
            break
    else:
        continue
    break

size, kill_cnt = 2, 0
time = 0
while True:
    find_result = find_next_monster()
    if not find_result:
        break
    moving_time, my, mx = find_result

    area[my][mx] = 0
    ry, rx = my, mx
    time += moving_time
    kill_cnt += 1
    if kill_cnt == size:
        size += 1
        kill_cnt = 0

print(time)
