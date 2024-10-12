# 20241012
# 34:02
# 1 / 1

"""
풀이 시간: 34분 (18:22 - 18:56)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (18:22 - 18:33)


2. 구현 (18:33 - 18:50)


3. 디버깅 (18:50 - 18:52)


4. 검증 (18:52 - 18:56)
    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    X (3) (머릿속 환기 후) 문제 재정독
    X (4) 커스텀 테스트케이스 검증
    X (5) 철저한 코드 검증
    X (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서


def can_move_south(y, x):
    if area[y + 1][x - 1] or area[y + 2][x] or area[y + 1][x + 1]:
        return False
    return True


def can_move_west_south(y, x):
    if area[y - 1][x - 1] or area[y][x - 2] or area[y + 1][x - 2] or area[y + 1][x - 1] or area[y + 2][x - 1]:
        return False
    return True


def can_move_east_south(y, x):
    if area[y - 1][x + 1] or area[y][x + 2] or area[y + 1][x + 2] or area[y + 1][x + 1] or area[y + 2][x + 1]:
        return False
    return True


def move_golem(s_c, s_d_idx):
    y, x = 1, s_c
    exit_d_idx = s_d_idx

    while True:
        if can_move_south(y, x):
            y += 1
            continue
        elif can_move_west_south(y, x):
            y += 1
            x -= 1
            exit_d_idx = (exit_d_idx - 1) % 4
            continue
        elif can_move_east_south(y, x):
            y += 1
            x += 1
            exit_d_idx = (exit_d_idx + 1) % 4
            continue
        else:
            break

    return y, x, exit_d_idx


def move_fairy(sy, sx):
    visited = [[0] * (c + 2) for _ in range(r + 4)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    deepest = sy + 1

    while queue:
        y, x = queue.popleft()
        deepest = max(deepest, y)

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if area[ny][nx] in (0, -1) or visited[ny][nx]:
                continue

            if area[y][x] in (1, 3):
                visited[ny][nx] = 1
                queue.append((ny, nx))
            elif area[y][x] == 2 and area[ny][nx] == 1:
                visited[ny][nx] = 1
                queue.append((ny, nx))

    return deepest - 2


r, c, k = map(int, input().split())
golems_start_info = [tuple(map(int, input().split())) for _ in range(k)]

area = [[-1] + [0] * c + [-1] for _ in range(r + 3)] + [[-1] * (c + 2)]

answer = 0
for start_column, start_d_idx in golems_start_info:
    end_row, end_column, end_d_idx = move_golem(start_column, start_d_idx)

    if end_row <= 3:
        area = [[-1] + [0] * c + [-1] for _ in range(r + 3)] + [[-1] * (c + 2)]
        continue

    area[end_row][end_column] = 1
    area[end_row][end_column + 1] = 2
    area[end_row][end_column - 1] = 2
    area[end_row + 1][end_column] = 2
    area[end_row - 1][end_column] = 2
    exit_r, exit_c = end_row + direction[end_d_idx][0], end_column + direction[end_d_idx][1]
    area[exit_r][exit_c] = 3

    answer += move_fairy(end_row, end_column)

print(answer)
