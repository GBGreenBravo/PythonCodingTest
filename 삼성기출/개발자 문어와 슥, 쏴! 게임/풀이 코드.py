from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상하좌우 우선순위


def oob(y, x):
    return y < 0 or M <= y or x < 0 or N <= x


# 현재 플레이어 1칸 이동시키는 함수
def move(p_idx):
    global first_getter, getter_cnt

    # 시작 좌표 (= 플레이어의 현재 좌표)
    sy, sx = players[p_idx][:-1]

    # 방문배열 & BFS용 queue
    visited = [[0] * N for _ in range(M)]
    visited[sy][sx] = 1
    queue = deque()

    # 상하좌우 우선순위대로 초기 queue에 넣기
    for d_idx, (dy, dx) in enumerate(direction):
        ny, nx = sy + dy, sx + dx
        if oob(ny, nx) or area[ny][nx] == 1:
            continue

        # 1칸 이동으로 보물(2)에 도착하는 경우
        if area[ny][nx] == 2:
            players[p_idx] = None      # 이동할 필요 없으니, 플레이어 정보 배열에 None으로 변경
            if not first_getter:       # 첫 보물 획득자라면, 번호 저장
                first_getter = p_idx
            getter_cnt += 1            # 보물 획득자 수 += 1
            return False               # 폭탄공격 수행 안 하도록 return False

        visited[ny][nx] = 1
        queue.append((ny, nx, d_idx))

    # BFS
    while queue:
        y, x, start_d = queue.popleft()

        # 보물(2)에 도착했다면
        if area[y][x] == 2:
            # 최단거리 시작 방향(start_d)으로 이동하고, 해당 정보를 players(플레이어 정보 배열)에 저장
            dy, dx = direction[start_d]
            ny, nx = sy + dy, sx + dx
            players[p_idx][0], players[p_idx][1] = ny, nx
            return True  # 폭탄 공격 수행해야 하므로 return True

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, start_d))

    return False  # 보물로 이동 못한다면, 폭탄공격 수행 안 하도록 return False


# 방금 이동한 플레이어가 폭탄공격 시도하는 함수
def bomb(p_idx):
    # 현재 좌표 & 남은 폭탄 수
    py, px, remain_bomb = players[p_idx]

    # 남은 폭탄이 없다면 바로 return
    if not remain_bomb:
        return

    # 폭탄 공격 가능한 곳들을 (distance, -행번호, -열번호, 행번호, 열번호)로 담을 배열
    possibles = []

    # 플레이어 정보배열 반복하며,
    for other_idx in range(1, K + 1):
        # (이미 격자 밖인 or 방금 이동한) 플레이어면 -> continue
        if not players[other_idx] or p_idx == other_idx:
            continue

        # 다른 플레이어 좌표
        oy, ox = players[other_idx][:-1]

        # 다른 플레이어와 상하좌우 직선상에 없다면 or 현재 플레이어와 같은 좌표에 있다면 -> continue
        if (py == oy and px == ox) or not (py == oy or px == ox):
            continue

        # 다른 플레이어와의 방향(상하좌우) 구하기
        dy, dx = 0, 0
        if oy - py:
            if oy - py > 0:
                dy = 1
            else:
                dy = -1
        if ox - px:
            if ox - px > 0:
                dx = 1
            else:
                dx = -1

        # 두 플레이어 사이에 벽 있는지 판단
        y, x = py + dy, px + dx
        while (y, x) != (oy, ox):
            # 벽이 있거나 or 사정거리 벗어난다면 -> break
            if area[y][x] == 1 or (abs(y - py) + abs(x - px) == B):
                break
            y, x = y + dy, x + dx
        else:  # 두 플레이어 사이에 벽 없고 & 사정거리(B) 이내라면 -> 폭탄 공격 가능한 곳
            distance = abs(oy - ey) + abs(ox - ex)          # distance : 보물 좌표와의 맨해튼 거리
            possibles.append((distance, -oy, -ox, oy, ox))  # 우선순위대로 담기 (distance, -행번호, -열번호, 행번호, 열번호)

    # 폭탄 공격 가능한 곳 없다면 -> return
    if not possibles:
        return

    # 폭탄공격할 좌표
    ty, tx = min(possibles)[-2:]

    # 임시벽 세우기
    walls.append((ty, tx, D, p_idx))  # 임시벽 세운 좌표(ty, tx) & 임시벽 내구도 & 누구로 인해 만들어졌는지
    area[ty][tx] = 1

    # 현재 플레이어 폭탄 개수 -= 1
    players[p_idx][-1] -= 1

    # 폭탄공격할 좌표에 있는 플레이어 -> 이탈 처리
    for other_idx in range(1, K + 1):
        if not players[other_idx] or p_idx == other_idx:  # 이미 격자 밖 or 현재 플레이어 -> continue
            continue
        oy, ox = players[other_idx][:-1]
        if (oy, ox) == (ty, tx):  # 이탈 처리
            players[other_idx] = None


# 플레이어 이동 후, 벽의 내구도 감소시키는 함수
def decrease_walls(p_idx):
    global walls

    next_walls = []
    for y, x, life, made_by in walls:
        if made_by == p_idx:  # 방금 이동한 플레이어가 만든 임시벽이면 -> 내구도 감소 X
            next_walls.append((y, x, life, made_by))
        elif life == 1:       # 이제 0으로 되는 임시벽이면 -> 빈칸(0)으로 복구
            area[y][x] = 0
        else:                 # 내구도 감소
            next_walls.append((y, x, life - 1, made_by))
    walls = next_walls


# 좌표를 받아, 회전하는 영역 내에 있는지 판단하는 함수
def in_rotated_area(y, x):
    return (uly <= y < uly + R) and (ulx <= x < ulx + R)


# 한 턴의 모든 플레이어 이동이 끝나고, 영역을 회전시키는 함수
def rotate_area():
    global walls

    # area(격자) 돌리기
    rotating = [[area[uly + dy][ulx + dx] for dx in range(R)] for dy in range(R)]
    rotating = [list(row)[::-1] for row in zip(*rotating)]
    for dy in range(R):
        for dx in range(R):
            area[uly + dy][ulx + dx] = rotating[dy][dx]

    # players(플레이어 정보 배열) 돌리기
    for p_idx in range(1, K + 1):
        if not players[p_idx]:
            continue
        py, px = players[p_idx][:-1]
        if in_rotated_area(py, px):
            dy, dx = py - ey, px - ex
            ny, nx = ey + dx, ex - dy
            players[p_idx][0], players[p_idx][1] = ny, nx

    # walls(임시벽 정보 배열) 돌리기
    next_walls = []
    for wy, wx, life, made_by in walls:
        if not in_rotated_area(wy, wx):
            next_walls.append((wy, wx, life, made_by))
            continue
        dy, dx = wy - ey, wx - ex
        ny, nx = ey + dx, ex - dy
        next_walls.append((ny, nx, life, made_by))
    walls = next_walls


T = int(input())
for test in range(1, T + 1):
    M, N = map(int, input().split())
    K, B, D, R = map(int, input().split())  # 참가자 수 / 폭탄 사정거리 / 벽 유지 기간 / 회전배열 길이
    area = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if area[i][j] == 2:
                ey, ex = i, j                      # 보물 좌표 구하기
                uly, ulx = i - R // 2, j - R // 2  # 회전하는 좌상단 좌표 구하기
                break
        else:
            continue
        break

    # 플레이어 정보 배열
    players = [None]
    for _ in range(K):
        aa, bb, cc = map(int, input().split())
        players.append([aa - 1, bb - 1, cc])  # [행 좌표, 열 좌표, 폭탄 개수]

    # 임시벽 정보 배열
    walls = []

    # 정답 출력을 위한, 첫 획득 플레이어 번호 & 보물 획득 플레이어 수
    first_getter, getter_cnt = 0, 0

    turn = 1
    while turn <= 1000:
        this_turn_moved = False  # 이번 턴에 1명이라도 움직였는지 파악하기 위한 flag

        # 각 플레이어 이동 시도
        for player_idx in range(1, K + 1):
            if not players[player_idx]:      # 이동 못하면(보물 획득 or 폭탄 공격 받음) -> continue
                continue

            if move(player_idx):             # 이동 시도해보고, 이동 했다면
                this_turn_moved = True       # 이동 flag = True
                bomb(player_idx)             # 폭탄 공격 시도

            if players[player_idx]:          # 보물 획득했다면 decrease_walls() 하지 않음
                decrease_walls(player_idx)

        # 아무도 이번 턴에 안 움직였거나, 모두 (보물 획득 or 폭탄 공격 받음) 라면 -> break
        if not this_turn_moved or not sum([bool(player) for player in players]):
            break

        # 배열 회전
        rotate_area()

        turn += 1

    if turn == 1001 or not getter_cnt:  # 1000턴까지 수행해도 게임이 안 끝나거나, 아무도 보물 획득 못 했다면 -> -1 출력
        print(f"#{test} -1")
    else:                               # " 정상적으로 게임 종료됐다면 -> 첫 획득 플레이어 번호 & 보물 획득 플레이어 수 & 진행된 턴 수 " 출력
        print(f"#{test} {first_getter} {getter_cnt} {turn}")
