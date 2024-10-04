# 20241004
# 44:36
# 1 / 1

# 21611_마법사상어와블리자드

"""
풀이 시간: 45분 (14:55 - 15:40)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:55 - 15:01)
    이전 풀이와 풀이방식이 매우 달랐습니다.
    이전 풀이에서는 연속하는 구슬들을 deque에 담아서 deque의 index를 기준으로 구상했고,
    이번 풀이에서는 N*N배열 area의 칸별 index를 기준으로 구상했습니다.


2. 구현 (15:01 - 15:25)
    늘 하던 대로 route에 나선형 회전 좌표(중심좌표 제외)들을 넣어줬습니다.
    중력을 작용하는 코드와 마찬가지로 route의 index를 하나씩 늘리며 몬스터들 사이 빈 공간을 채웠습니다.

    이전 풀이보다 코드가 더 길지만, 다른 구상으로도 단번에 정확하게 맞췄다는 의의가 있었습니다.


3. 디버깅 (15:25 - 15:39)
    같은 몬스터 종류가 연속 4개 이상일 때, 삭제해주는 과정에서 문제가 있음을 print/디버그모드 를 통해 확인했습니다.
    기존 배열의 값과 다를 때, "now_line = [now]"로 재선언 해야할 것을
    "now_line = []"으로 재선언한 것으로부터 비롯된 이슈임을 파악하고 수정했습니다.
"""

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_monsters():
    global area

    new_area = [[0] * n for _ in range(n)]

    route_idx = 0
    for ry, rx in route:
        now = area[ry][rx]
        if not now:
            continue
        nry, nrx = route[route_idx]
        new_area[nry][nrx] = now
        route_idx += 1

    area = new_area


def delete_above_four_in_a_row():
    global area, total_score

    deleted_flag = False

    line = []
    now_line = []
    for ry, rx in route:
        now = area[ry][rx]

        if not now:
            break

        if not now_line:
            now_line.append(now)
        elif now_line[-1] == now:
            now_line.append(now)
        else:
            if len(now_line) < 4:
                line.extend(now_line)
            else:
                total_score += len(now_line) * now_line[0]
                deleted_flag = True
            now_line = [now]
    if now_line and len(now_line) < 4:
        line.extend(now_line)
    elif now_line:
        total_score += len(now_line) * now_line[0]
        deleted_flag = True

    new_area = [[0] * n for _ in range(n)]
    r_idx = 0
    for line_value in line:
        nry, nrx = route[r_idx]
        new_area[nry][nrx] = line_value
        r_idx += 1

    area = new_area

    return deleted_flag


def realign_monsters():
    global area

    line = []
    now_line = []
    for ry, rx in route:
        now = area[ry][rx]

        if not now:
            break

        if not now_line:
            now_line.append(now)
        elif now_line[-1] == now:
            now_line.append(now)
        else:
            line.extend([len(now_line), now_line[0]])
            now_line = [now]
    if now_line and len(now_line) < 4:
        line.extend([len(now_line), now_line[0]])

    new_area = [[0] * n for _ in range(n)]
    r_idx = 0
    for line_value in line:
        if r_idx == len(route):
            break
        nry, nrx = route[r_idx]
        new_area[nry][nrx] = line_value
        r_idx += 1

    area = new_area


n, m = map(int, input().split())

route = []
spiral_visited = [[0] * n for _ in range(n)]
si, sj, sd = 0, 0, 0

while not (si == n // 2 and sj == n // 2):
    route.append((si, sj))
    spiral_visited[si][sj] = 1

    dsi, dsj = direction[sd]
    nsi, nsj = si + dsi, sj + dsj
    if oob(nsi, nsj) or spiral_visited[nsi][nsj]:
        sd = (sd + 1) % 4
        dsi, dsj = direction[sd]
        nsi, nsj = si + dsi, sj + dsj
    si, sj = nsi, nsj
route.reverse()

area = [list(map(int, input().split())) for _ in range(n)]
attack_infos = [tuple(map(int, input().split())) for _ in range(m)]

total_score = 0

for attack_d, attack_range in attack_infos:
    cy, cx = n // 2, n // 2
    dcy, dcx = direction[attack_d]
    for attack_r in range(1, attack_range + 1):
        attacked_value = area[cy + dcy * attack_r][cx + dcx * attack_r]
        if attacked_value:
            total_score += attacked_value
            area[cy + dcy * attack_r][cx + dcx * attack_r] = 0

    move_monsters()
    deleted = delete_above_four_in_a_row()
    while deleted:
        # move_monsters()
        deleted = delete_above_four_in_a_row()

    realign_monsters()

print(total_score)
