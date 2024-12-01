from collections import deque

direction_4 = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상하좌우
direction_8 = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))  # 0상 1하 2좌 3우 4상좌 5상우 6하좌 7하우


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def find_m_route():
    visited = [[0] * N for _ in range(N)]
    visited[my][mx] = 1
    queue = deque()
    queue.append((my, mx, [(my, mx)]))
    while queue:
        y, x, route = queue.popleft()
        if (y, x) == (ey, ex):
            return route
        for dy, dx in direction_4:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, route + [(ny, nx)]))
    return None


# 현재 좌표(init_y, init_x)와 방향에 의해 가려지는 좌표들 반환하는 함수
def get_shadow_indexes(init_y, init_x, middle_d, start_d, end_d):  # 0상 1하 2좌 3우 4상좌 5상우 6하좌 7하우
    indexes = set()

    dy, dx = direction_8[middle_d]      # 영역 밖으로 나가는지 탐색하기 위한 좌표
    sdy, sdx = direction_8[start_d]     # for문용 처음 좌표
    edy, edx = direction_8[end_d]       # for문용 마지막 좌표
    # 시야 방향으로 1칸 가보기
    y, x = init_y + dy, init_x + dx
    sy, sx = init_y + sdy, init_x + sdx
    ey, ex = init_y + edy, init_x + edx
    # 중심 좌표가 영역밖으로 나갈때까지
    while not oob(y, x):
        if dx == 0:
            for xx in range(max(0, sx), min(N, ex + 1)):
                indexes.add((y, xx))
        else:
            for yy in range(max(0, sy), min(N, ey + 1)):
                indexes.add((yy, x))

        y, x = y + dy, x + dx
        sy, sx = sy + sdy, sx + sdx
        ey, ex = ey + edy, ex + edx
    return indexes


# 메두사 시선 정하고, (메두사 시선 좌표들, 돌로 변한 좌표들) 반환하는 함수
def get_m_sight():
    global rock_cnt

    candidates = []
    for middle_d, start_d, end_d in ((0, 4, 5), (1, 6, 7), (2, 4, 6), (3, 5, 7)):  # 0상 1하 2좌 3우 4상좌 5상우 6하좌 7하우
        sight = set()      # 메두사 시선 좌표들
        stun_cnt = 0       # 돌로 변할 전사들 수
        stun_indexes = []  # 돌로 변할 좌표들
        shadow = set()     # 돌로 인해 가려지는 좌표들

        dy, dx = direction_8[middle_d]      # 영역 밖으로 나가는지 탐색하기 위한 좌표
        sdy, sdx = direction_8[start_d]     # for문용 처음 좌표
        edy, edx = direction_8[end_d]       # for문용 마지막 좌표
        # 시야 방향으로 1칸 가보기
        y, x = my + dy, mx + dx
        sy, sx = my + sdy, mx + sdx
        ey, ex = my + edy, mx + edx
        # 중심 좌표가 영역밖으로 나갈때까지
        while not oob(y, x):
            if dx == 0:
                for xx in range(max(0, sx), min(N, ex + 1)):
                    if (y, xx) in shadow:  # 현재 좌표가 그림자에 해당되는 곳이면 -> continue
                        continue
                    sight.add((y, xx))     # 시야 내 좌표로 추가
                    # 현재 칸에 전사 있다면
                    if warriors_area[y][xx]:
                        stun_cnt += warriors_area[y][xx]  # 돌로 변할 전사들 수 += 현재 칸 전사들 수
                        stun_indexes.append((y, xx))      # 돌로 변할 좌표들에 추가
                        # 그림자 좌표 구하기
                        if xx == x:
                            shadow_indexes = get_shadow_indexes(y, xx, middle_d, middle_d, middle_d)
                        elif xx < x:
                            shadow_indexes = get_shadow_indexes(y, xx, middle_d, start_d, middle_d)
                        else:
                            shadow_indexes = get_shadow_indexes(y, xx, middle_d, middle_d, end_d)
                        shadow.update(shadow_indexes)     # 돌로 인해 가려지는 좌표들에 그림자 좌표들 추가
            else:
                for yy in range(max(0, sy), min(N, ey + 1)):
                    if (yy, x) in shadow:
                        continue
                    sight.add((yy, x))
                    if warriors_area[yy][x]:
                        stun_cnt += warriors_area[yy][x]
                        stun_indexes.append((yy, x))
                        if yy == y:
                            shadow_indexes = get_shadow_indexes(yy, x, middle_d, middle_d, middle_d)
                        elif yy < y:
                            shadow_indexes = get_shadow_indexes(yy, x, middle_d, start_d, middle_d)
                        else:
                            shadow_indexes = get_shadow_indexes(yy, x, middle_d, middle_d, end_d)
                        shadow.update(shadow_indexes)
            y, x = y + dy, x + dx
            sy, sx = sy + sdy, sx + sdx
            ey, ex = ey + edy, ex + edx

        candidates.append((-stun_cnt, middle_d, sight, stun_indexes))

    minus_stun_cnt, _, sights, stun_indexes = min(candidates)  # 우선순위 : (돌로 변한 전사들 수 내림차순, 상하좌우순)
    rock_cnt = -minus_stun_cnt   # 돌로 변한 전사들 추가
    return sights, stun_indexes  # (메두사 시선 좌표들, 돌로 변한 좌표들) 반환


# 전사들 이동시키는 함수
def warriors_move_and_attack():
    global warriors_area, total_move_cnt, attack_cnt

    # 전사들 이동 후 상태가 담길 배열
    next_warriors_area = [[0] * N for _ in range(N)]
    for sy in range(N):
        for sx in range(N):
            # 현재 칸에 전사 있다면
            if warriors_area[sy][sx]:
                # 돌로 변해있는 전사들이면 -> 이동 X
                if (sy, sx) in stunned_warriors:
                    next_warriors_area[sy][sx] += warriors_area[sy][sx]
                    continue

                # 1번째 이동 시도
                first_candidates = []
                for d_idx, (dy, dx) in enumerate(direction_4):
                    ny, nx = sy + dy, sx + dx
                    if oob(ny, nx) or (ny, nx) in m_sight or abs(my - sy) + abs(mx - sx) <= abs(my - ny) + abs(mx - nx):
                        continue
                    first_candidates.append((d_idx, ny, nx))
                if not first_candidates:                 # 이동가능한 좌표 없다면 -> 이동 X
                    next_warriors_area[sy][sx] += warriors_area[sy][sx]
                    continue
                _, fy, fx = min(first_candidates)
                total_move_cnt += warriors_area[sy][sx]  # 현재턴 전체 움직임 수 += 움직이는 전사 수
                if (fy, fx) == (my, mx):                 # 1번 움직임으로 메두사에게 닿았다면 -> 현재턴 전체 공격자 수 += 움직인 전사 수
                    attack_cnt += warriors_area[sy][sx]
                    continue

                # 2번째 이동 시도
                second_candidates = []
                for d_idx, (dy, dx) in enumerate(direction_4):
                    ny, nx = fy + dy, fx + dx
                    if oob(ny, nx) or (ny, nx) in m_sight or abs(my - fy) + abs(mx - fx) <= abs(my - ny) + abs(mx - nx):
                        continue
                    if d_idx <= 1:  # 상 하 -> 4 5
                        second_candidates.append((d_idx + 4, ny, nx))
                    else:           # 좌 우 -> 2 3
                        second_candidates.append((d_idx, ny, nx))
                if not second_candidates:                # 이동가능한 좌표 없다면 -> 첫번째 움직임 좌표(fy, fx)로 이동
                    next_warriors_area[fy][fx] += warriors_area[sy][sx]
                    continue
                _, ly, lx = min(second_candidates)
                total_move_cnt += warriors_area[sy][sx]  # 현재 턴 전체 움직임 수 += 움직이는 전사 수
                if (ly, lx) == (my, mx):                 # 2번 움직임으로 메두사에게 닿았다면 -> 현재턴 전체 공격자 수 += 움직인 전사 수
                    attack_cnt += warriors_area[sy][sx]
                    continue
                next_warriors_area[ly][lx] += warriors_area[sy][sx]  # 2번 움직인 좌표(ly, lx)로 이동

    warriors_area = next_warriors_area


N, M = map(int, input().split())
my, mx, ey, ex = map(int, input().split())
warriors_input = list(map(int, input().split()))
warriors_area = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    wi, wj = warriors_input[i * 2: i * 2 + 2]
    warriors_area[wi][wj] += 1
area = [list(map(int, input().split())) for _ in range(N)]

m_route = find_m_route()
if not m_route:  # 메두사가 공원으로 가는 경로 존재하지 않으면, -1 출력
    print(-1)
else:
    for my, mx in m_route[1:-1]:  # 메두사의 중간루트에 대해서
        total_move_cnt, rock_cnt, attack_cnt = 0, 0, 0    # 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수
        warriors_area[my][mx] = 0                         # 메두사가 이동한 곳의 전사들 사라짐
        m_sight, stunned_warriors = get_m_sight()         # 메두사 시선 좌표들, 돌로 변한 좌표들
        warriors_move_and_attack()                        # 전사들 이동
        print(total_move_cnt, rock_cnt, attack_cnt)       # 현재 턴 정답 출력
    print(0)  # 마지막 턴(공원 도착하는 턴)에 0 출력
