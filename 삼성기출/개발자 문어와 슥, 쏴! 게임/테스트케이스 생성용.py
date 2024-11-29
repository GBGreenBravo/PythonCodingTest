from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))


def oob(y, x):
    return y < 0 or M <= y or x < 0 or N <= x


def move(p_idx):
    global first_getter, getter_cnt

    sy, sx = players[p_idx][:-1]
    visited = [[0] * N for _ in range(M)]
    visited[sy][sx] = 1
    queue = deque()
    for d_idx, (dy, dx) in enumerate(direction):
        ny, nx = sy + dy, sx + dx
        if oob(ny, nx) or area[ny][nx] == 1:
            continue

        if area[ny][nx] == 2:
            players[p_idx] = None
            if not first_getter:
                first_getter = p_idx
            getter_cnt += 1
            return False

        visited[ny][nx] = 1
        queue.append((ny, nx, d_idx))

    while queue:
        y, x, start_d = queue.popleft()
        if area[y][x] == 2:
            dy, dx = direction[start_d]
            ny, nx = sy + dy, sx + dx
            players[p_idx][0], players[p_idx][1] = ny, nx
            return True

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx, start_d))

    return False


def bomb(p_idx):
    global total_killed_cnt

    possibles = []
    py, px, remain_bomb = players[p_idx]
    if not remain_bomb:
        return

    for other_idx in range(1, K + 1):
        if not players[other_idx] or p_idx == other_idx:
            continue
        oy, ox = players[other_idx][:-1]
        if (py == oy and px == ox) or not (py == oy or px == ox):
            continue
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

        y, x = py + dy, px + dx
        while (y, x) != (oy, ox):
            if area[y][x] == 1 or (abs(y - py) + abs(x - px) == B):
                break
            y, x = y + dy, x + dx
        else:
            distance = abs(oy - ey) + abs(ox - ex)
            possibles.append((distance, -oy, -ox, oy, ox))

    if not possibles:
        return

    ty, tx = min(possibles)[-2:]

    walls.append((ty, tx, D, p_idx))
    area[ty][tx] = 1

    players[p_idx][-1] -= 1

    for other_idx in range(1, K + 1):
        if not players[other_idx] or p_idx == other_idx:
            continue
        oy, ox = players[other_idx][:-1]
        if (oy, ox) == (ty, tx):
            players[other_idx] = None
            # print(str(p_idx) + " -- killed -> " + str(other_idx))
            total_killed_cnt += 1


def decrease_walls(p_idx):
    global walls

    next_walls = []
    for y, x, life, made_by in walls:
        if made_by == p_idx:
            next_walls.append((y, x, life, made_by))
        elif life == 1:
            area[y][x] = 0
        else:
            next_walls.append((y, x, life - 1, made_by))
    walls = next_walls


def in_rotated_area(y, x):
    return (uly <= y < uly + R) and (ulx <= x < ulx + R)


def rotate_area():
    global walls

    # area 돌리기
    rotating = [[area[uly + dy][ulx + dx] for dx in range(R)] for dy in range(R)]
    rotating = [list(row)[::-1] for row in zip(*rotating)]
    for r in range(R):
        for c in range(R):
            area[uly + r][ulx + c] = rotating[r][c]

    # players 돌리기
    for p_idx in range(1, K + 1):
        if not players[p_idx]:
            continue
        py, px = players[p_idx][:-1]
        if in_rotated_area(py, px):
            dy, dx = py - ey, px - ex
            ny, nx = ey + dx, ex - dy
            players[p_idx][0], players[p_idx][1] = ny, nx

    # walls 돌리기
    next_walls = []
    for wy, wx, life, made_by in walls:
        if not in_rotated_area(wy, wx):
            next_walls.append((wy, wx, life, made_by))
            continue
        dy, dx = wy - ey, wx - ex
        ny, nx = ey + dx, ex - dy
        next_walls.append((ny, nx, life, made_by))
    walls = next_walls
    return


T = int(input())
for test in range(1, T + 1):
    M, N = map(int, input().split())
    K, B, D, R = map(int, input().split())  # 참가자 수 / 폭탄 사정거리 / 벽 유지 기간 / 회전배열 길이
    area = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if area[i][j] == 2:
                ey, ex = i, j
                uly, ulx = i - R // 2, j - R // 2
                break
        else:
            continue
        break

    players = [None]
    for _ in range(K):
        aa, bb, cc = map(int, input().split())
        if area[aa - 1][bb - 1]:
            raise RuntimeError((aa - 1, bb - 1), "은 값이 0이어야 됨!")
        players.append([aa - 1, bb - 1, cc])

    total_killed_cnt = 0

    first_getter, getter_cnt = 0, 0
    walls = []
    turn = 1
    while turn <= 1000:
        this_turn_moved = False

        # print()
        # print(turn)
        # print("before moving")
        # print(*players, sep="\n")
        # print_area = [row[:] for row in area]
        # for pii in range(1, K + 1):
        #     if players[pii]:
        #         print_area[players[pii][0]][players[pii][1]] = "|" + str(pii) + "|"
        # for prow in print_area:
        #     for pitem in prow:
        #         if str(pitem)[-1] != '|':
        #             print(" " + str(pitem) + " ", end=" ")
        #         else:
        #             print(str(pitem), end=" ")
        #     print()
        # print("walls:", walls)

        for player_idx in range(1, K + 1):
            if not players[player_idx]:
                continue
            if move(player_idx):
                this_turn_moved = True
                bomb(player_idx)
            if players[player_idx]:
                decrease_walls(player_idx)

        # print("after moving")
        # print(*players, sep="\n")
        # print_area = [row[:] for row in area]
        # for pii in range(1, K + 1):
        #     if players[pii]:
        #         print_area[players[pii][0]][players[pii][1]] = "|" + str(pii) + "|"
        # for prow in print_area:
        #     for pitem in prow:
        #         if str(pitem)[-1] != '|':
        #             print(" " + str(pitem) + " ", end=" ")
        #         else:
        #             print(str(pitem), end=" ")
        #     print()

        if not this_turn_moved or not sum([bool(player) for player in players]):
            break

        rotate_area()

        turn += 1

    # print("total_killed_cnt:", total_killed_cnt)
    if turn == 1001 or not getter_cnt:
        print(f"#{test} -1")
    else:
        print(f"#{test} {first_getter} {getter_cnt} {turn}")


# input()
# M, N = map(int, input().split())
# input()
# area = [list(map(int, input().split())) for _ in range(M)]
# points = set()
# for i in range(M):
#     for j in range(N):
#         if area[i][j] == 3:
#             points.add((i, j))
# for y, x in points:
#     print(y + 1, x + 1)
