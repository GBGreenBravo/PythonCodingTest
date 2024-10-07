# 20241007
# 50:26
# 1 / 1

"""
풀이 시간: 50분 (16:32 - 17:22)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:32 - 16:39)


2. 구현 (16:39 - 16:57)
    이전 풀이와 다른 부분은, 십자가 부분의 회전과 맞닿는 변 수 계산 부분이었습니다.
    이렇게 코드리뷰에서 본 방식으로 구현하니, 여러 풀이방식이 생각나게 된다는 장점이 있는 듯 합니다.

    그리고 이전보다 함수화의 단위가 더 커졌는데, 각각의 장단점이 있는 것 같습니다.
    함수가 더 잘게 쪼개지면, 해당 모듈의 단위 테스트에 용이하다는 장점이 있고,
    함수가 큰 단위로 작성되면, 그 함수의 로직을 한 눈에 볼 수 있다는 장점이 있습니다.

    최근 기출문제들을 반복적으로 빨리 풀면서, 함수를 너무 잘게는 안 나누는 것 같은데,
    나중에 본시험에서 단위테스트만 잘 해준다면 문제는 없을 것으로 생각합니다.


3. 디버깅 (16:57 - 16:58)


4. 검증 (16:58 - 17:22)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def rotate_area():
    top_left = [area[row][:n // 2] for row in range(n // 2)]
    top_right = [area[row][n // 2 + 1:] for row in range(n // 2)]
    bottom_left = [area[row][:n // 2] for row in range(n // 2 + 1, n)]
    bottom_right = [area[row][n // 2 + 1:] for row in range(n // 2 + 1, n)]

    top_left = [list(row)[::-1] for row in zip(*top_left)]
    top_right = [list(row)[::-1] for row in zip(*top_right)]
    bottom_left = [list(row)[::-1] for row in zip(*bottom_left)]
    bottom_right = [list(row)[::-1] for row in zip(*bottom_right)]

    for row in range(n // 2):
        for col in range(n // 2):
            area[row][col] = top_left[row][col]
            area[row][n // 2 + 1 + col] = top_right[row][col]
            area[n // 2 + 1 + row][col] = bottom_left[row][col]
            area[n // 2 + 1 + row][n // 2 + 1 + col] = bottom_right[row][col]

    up_y, up_x = n // 2, n // 2
    right_y, right_x = n // 2, n // 2
    down_y, down_x = n // 2, n // 2
    left_y, left_x = n // 2, n // 2
    for i in range(n // 2):
        up_y -= 1
        right_x += 1
        down_y += 1
        left_x -= 1
        area[up_y][up_x], area[right_y][right_x], area[down_y][down_x], area[left_y][left_x] = \
            area[right_y][right_x], area[down_y][down_x], area[left_y][left_x], area[up_y][up_x]


def cal_art_score():
    group_visited = [[0] * n for _ in range(n)]
    group_infos = [None]
    group_flag = 0

    for sy in range(n):
        for sx in range(n):
            if not group_visited[sy][sx]:
                group_flag += 1
                group_value = area[sy][sx]
                group_cnt = 1

                group_visited[sy][sx] = group_flag

                queue = deque()
                queue.append((sy, sx))

                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or group_visited[ny][nx] or area[ny][nx] != group_value:
                            continue
                        group_visited[ny][nx] = group_flag
                        queue.append((ny, nx))
                        group_cnt += 1

                group_infos.append((group_value, group_cnt))

    group_nears = [None] + [[0] * (group_flag + 1) for _ in range(group_flag)]
    for y in range(n):
        for x in range(n):
            for dy, dx in direction[:2]:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or group_visited[y][x] == group_visited[ny][nx]:
                    continue
                group_nears[group_visited[y][x]][group_visited[ny][nx]] += 1
                group_nears[group_visited[ny][nx]][group_visited[y][x]] += 1

    now_art_score = 0
    for a in range(1, group_flag):
        for b in range(a + 1, group_flag + 1):
            if not group_nears[a][b]:
                continue
            now_art_score += (group_infos[a][1] + group_infos[b][1]) * group_infos[a][0] * group_infos[b][0] * group_nears[a][b]
    return now_art_score


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

total_score = cal_art_score()
for _ in range(3):
    rotate_area()
    total_score += cal_art_score()
print(total_score)
