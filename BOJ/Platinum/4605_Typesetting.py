# 20241202
# 3:35:28
# 1 / 9

"""
5
#.... ... ######
#.... #.. .....#
#.... #.. .....#
#.... #.. .....#
###.. #.. .....#

위 경우에 대해서, 2번째를 왼쪽/오른쪽으로 밀지에 따라 아래와 같이 2개의 답이 나뉘는데, 난 오른쪽으로 밀어서 틀림. (지문에 안 적혀있던 사항 ㅠ)

왼쪽으로 미는 경우    오른쪽으로 미는 경우
#.######          #.######
#...#..#          #....#.#
#...#..#          #....#.#
#...#..#          #....#.#
###.#..#          ###..#.#
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or M <= xx


def check_possible_left(idx):
    length = 100
    for yy, xx in group_indexes[idx]:
        now_l = 1
        while now_l < length:
            if oob(yy, xx - now_l) or (visited[yy][xx - now_l] and visited[yy][xx - now_l] != idx):
                length = now_l
                break
            now_l += 1
    only_oob = True
    for yy, xx in group_indexes[idx]:
        if not oob(yy, xx - length) and visited[yy][xx - length] and visited[yy][xx - length] != idx:
            only_oob = False
            break
    return length, only_oob


def check_possible_right(idx):
    length = 100
    for yy, xx in group_indexes[idx]:
        now_l = 1
        while now_l < length:
            if oob(yy, xx + now_l) or (visited[yy][xx + now_l] and visited[yy][xx + now_l] != idx):
                length = now_l
                break
            now_l += 1
    only_oob = True
    for yy, xx in group_indexes[idx]:
        if not oob(yy, xx + length) and visited[yy][xx + length] and visited[yy][xx + length] != idx:
            only_oob = False
            break
    return length, only_oob


def move_left(idx, length):
    next_indexes = []
    for yy, xx in group_indexes[idx]:
        visited[yy][xx] = 0
        next_indexes.append((yy, xx - length))
    group_indexes[idx] = next_indexes
    for yy, xx in next_indexes:
        visited[yy][xx] = idx

    for next_idx in range(1, group_cnt + 1):
        if idx == next_idx:
            continue
        possible_l, n_valid = check_possible_left(next_idx)
        if not n_valid and possible_l >= 3:
            move_left(next_idx, possible_l - 2)


def move_right(idx, length):
    next_indexes = []
    for yy, xx in group_indexes[idx]:
        visited[yy][xx] = 0
        next_indexes.append((yy, xx + length))
    group_indexes[idx] = next_indexes
    for yy, xx in next_indexes:
        visited[yy][xx] = idx

    for next_idx in range(1, group_cnt + 1):
        if idx == next_idx:
            continue
        possible_l, n_valid = check_possible_right(next_idx)
        if not n_valid and possible_l >= 3:
            move_right(next_idx, possible_l - 2)


tc = 0
while True:
    N = int(input())
    if not N:
        break
    tc += 1
    print(tc)

    area = [list(str(input())) for _ in range(N)]
    M = len(area[0])

    visited = [[0] * M for _ in range(N)]
    area_visited = [[0] * M for _ in range(N)]
    group_cnt = 0
    group_indexes = [None]
    group_infos = [None]
    for i in range(N):
        for j in range(M):
            if area[i][j] not in (' ', '.') and not visited[i][j]:
                group_cnt += 1
                visited[i][j] = group_cnt
                area_visited[i][j] = 1
                group_arr = [(i, j + 20)]
                group_info = [area[i][j]]
                queue = deque()
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or area_visited[ny][nx] or area[ny][nx] == ' ':
                            continue
                        area_visited[ny][nx] = 1
                        queue.append((ny, nx))
                        if area[ny][nx] == '.':
                            continue
                        visited[ny][nx] = group_cnt
                        group_arr.append((ny, nx + 20))
                        group_info.append(area[ny][nx])
                group_indexes.append(group_arr)
                group_infos.append(group_info)

    for i in range(N):
        for j in range(M):
            if area[i][j] == ' ':
                area[i][j] = '.'

    M += 20
    for i in range(N):
        area[i] = ['.'] * 20 + area[i]
        visited[i] = [0] * 20 + visited[i]

    M += 20
    for i in range(N):
        area[i].extend(['.'] * 20)
        visited[i].extend([0] * 20)
    for i in range(1, group_cnt + 1):
        p_l, not_valid = check_possible_right(i)
        if not not_valid and p_l >= 3:
            move_right(i, p_l - 2)

    for i in range(1, group_cnt + 1):
        p_l, not_valid = check_possible_left(i)
        if not not_valid and p_l >= 3:
            move_left(i, p_l - 2)

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = '.'
    for i in range(1, group_cnt + 1):
        for j in range(len(group_infos[i])):
            ii, jj = group_indexes[i][j]
            visited[ii][jj] = group_infos[i][j] if group_infos[i][j] != '0' else '.'

    while True:
        for i in range(N):
            if visited[i][0] != '.':
                break
        else:
            for i in range(N):
                visited[i].pop(0)
            continue
        break
    while True:
        for i in range(N):
            if visited[i][-1] != '.':
                break
        else:
            for i in range(N):
                visited[i].pop(-1)
            continue
        break

    for row in visited:
        print("".join(row))
