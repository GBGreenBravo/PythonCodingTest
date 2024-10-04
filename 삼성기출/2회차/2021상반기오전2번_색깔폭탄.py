# 20241004
# 25:21
# 1 / 1

# 21609_상어중학교

"""
풀이 시간: 25분 (14:19 - 14:44)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:19 - 14:25)
    배열의 크기를 생각했을 때, 폭탄묶음을 선택하는 과정에서 모두 다 넣어놓고 min()으로 비교해도 시간/메모리 복잡도 이슈는 없겠다고 판단했습니다.


2. 구현 (14:25 - 14:44)
    중력작용 구현에서, 초기에 빈 배열을 선언하고 한 행/열씩 추가하는 게 아니라,
    빈칸(-2)으로 전부 채워놓고 값을 넣어주는 index만 하나씩 조정하는 게 더 간편하고도 합리적인 코드라 생각이 들었습니다.
    앞으로도 '장애물이 있는 중력작용'에서는 이 방식을 채택하지 않을까 생각합니다.


3. 디버깅 (-)
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def find_biggest_group():
    candidates = []

    visited = [[0] * n for _ in range(n)]

    for sy in range(n):
        for sx in range(n):
            if not visited[sy][sx] and area[sy][sx] >= 1:
                visited[sy][sx] = 1

                queue = deque()
                queue.append((sy, sx))

                criteria = area[sy][sx]
                now_group = [(sy, sx)]
                now_red_cnt = 0
                now_standard_index = (-sy, sx)

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or area[ny][nx] < 0 or (ny, nx) in now_group:
                            continue

                        if area[ny][nx] == 0:
                            now_group.append((ny, nx))
                            queue.append((ny, nx))

                            now_red_cnt += 1
                        elif area[ny][nx] == criteria:
                            now_group.append((ny, nx))
                            queue.append((ny, nx))

                            visited[ny][nx] = 1
                            now_standard_index = min(now_standard_index, (-ny, nx))

                if len(now_group) > 1:
                    candidates.append((-len(now_group), now_red_cnt, now_standard_index[0], now_standard_index[1], now_group))

    if not candidates:
        return None
    else:
        return min(candidates)[-1]


def gravity():
    global area

    new_area = [[-2] * n for _ in range(n)]
    for col in range(n):
        now_row_idx = n - 1
        for row in range(n - 1, -1, -1):
            if area[row][col] == -2:
                continue
            elif area[row][col] == -1:
                new_area[row][col] = -1
                now_row_idx = row - 1
            else:
                new_area[now_row_idx][col] = area[row][col]
                now_row_idx -= 1

    area = new_area


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

total_score = 0
selected = find_biggest_group()
while selected:
    total_score += len(selected)**2
    for sel_y, sel_x in selected:
        area[sel_y][sel_x] = -2
    gravity()
    area = [list(row) for row in list(zip(*area))[::-1]]
    gravity()
    selected = find_biggest_group()
print(total_score)
