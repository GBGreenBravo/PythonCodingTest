# 20241011
# 1:18:00
# 1 / 1

"""
풀이 시간: 1시간 18분 (09:14 - 10:32)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (09:14 - 09:25)


2. 구현 (09:25 - 09:54)


3. 디버깅 (09:54 - 09:55)


4. 검증 (09:55 - 10:32)
    10시 27분에 꼼꼼히 코드를 정독하는 과정에서, 사소하지만 치명적인 오타를 발견했습니다.
    next_knight라고 써야 할 부분에 next_knights라고 써서, 기사가 여러 칸 이동할 여지가 있었습니다.
    따라서 해당 변수를 수정하고, 안전하게 return visited말고 return list(set(visited))로 반환했습니다.
    이러한 오타를 내지 않기 위해서, next_knight말고 n_knight와 같이
    변수 간의 구분을 더욱 원활히 할 수 있도록 명명해야겠습니다.

    단위테스트 위주로 커스텀 테케를 많이 만들어보며, 검증했습니다.

    O (1) 주어진 테스트케이스로 검증
    O (2) 메모 vs. 코드
    O (3) (머릿속 환기 후) 문제 재정독
    O (4) 커스텀 테스트케이스 검증
    O (5) 철저한 코드 검증
    O (6) 오답노트 활용
    X (7) 다양한 구상에 따른, 다른 구현
"""

from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌


def cal_next_line(row, col, height, width):
    if command_d == 0:
        return area[row - 1][col:col + width], knights_map[row - 1][col:col + width]
    elif command_d == 1:
        return [area[n_row][col + width] for n_row in range(row, row + height)], [knights_map[n_row][col + width] for n_row in range(row, row + height)]
    elif command_d == 2:
        return area[row + height][col:col + width], knights_map[row + height][col:col + width]
    elif command_d == 3:
        return [area[n_row][col - 1] for n_row in range(row, row + height)], [knights_map[n_row][col - 1] for n_row in range(row, row + height)]


def cal_moving_knights():
    visited = [command_knight]

    queue = deque()
    queue.append(command_knight)

    while queue:
        now_knight = queue.popleft()
        next_area_line, next_knights = cal_next_line(*knights_info[now_knight])

        if 2 in next_area_line:
            return None
        for next_knight in set(next_knights):
            if next_knight and next_knight not in visited:
                visited.append(next_knight)
                queue.append(next_knight)

    return list(set(visited))


l, n, q = map(int, input().split())
area = [[2] * (l + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(l)] + [[2] * (l + 2)]

knights_map = [[0] * (l + 2) for _ in range(l + 2)]
knights_life = [None]
knights_info = [None]
for k_input_index in range(1, n + 1):
    rr, cc, hh, ww, kk = map(int, input().split())
    for rh in range(rr, rr + hh):
        for cw in range(cc, cc + ww):
            knights_map[rh][cw] = k_input_index
    knights_info.append((rr, cc, hh, ww))
    knights_life.append(kk)
first_knights_life = [life_copy for life_copy in knights_life]

commands = [tuple(map(int, input().split())) for _ in range(q)]
for command_knight, command_d in commands:
    if not knights_info[command_knight]:
        continue

    dr, dc = direction[command_d]
    moving_knights = cal_moving_knights()
    if not moving_knights:
        continue

    for moving_knight in moving_knights:
        k_r, k_c, k_h, k_w = knights_info[moving_knight]
        for k_rh in range(k_r, k_r + k_h):
            for k_cw in range(k_c, k_c + k_w):
                knights_map[k_rh][k_cw] = 0
    for moving_knight in moving_knights:
        k_r, k_c, k_h, k_w = knights_info[moving_knight]
        knights_info[moving_knight] = k_r + dr, k_c + dc, k_h, k_w
        k_r, k_c, k_h, k_w = knights_info[moving_knight]

        damage = 0
        for k_rh in range(k_r, k_r + k_h):
            for k_cw in range(k_c, k_c + k_w):
                knights_map[k_rh][k_cw] = moving_knight
                if moving_knight != command_knight and area[k_rh][k_cw] == 1:
                    damage += 1

        knights_life[moving_knight] -= damage
        if knights_life[moving_knight] <= 0:
            knights_info[moving_knight] = None
            for k_rh in range(k_r, k_r + k_h):
                for k_cw in range(k_c, k_c + k_w):
                    knights_map[k_rh][k_cw] = 0

answer = 0
for k_index in range(1, n + 1):
    if knights_info[k_index]:
        answer += first_knights_life[k_index] - knights_life[k_index]
print(answer)
