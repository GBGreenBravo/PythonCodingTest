# 20241004
# 47:15
# 1 / 2

# 23289_온풍기안녕

"""
풀이 시간: 47분 (15:59 - 16:46)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (15:59 - 16:09)
    이전 풀이에서는 매초마다 온풍기에서 바람나오게 해서 추가되는 시원함을 계속 계산했었습니다.
    그러나 이번에 문제를 읽으면서, 온풍기에서 나오는 바람으로 인해 칸별 추가되는 시원함은 매번 동일함을 깨달았습니다.
    따라서, 미리 칸별 추가되는 시원함을 계산해놓고 풀기로 했습니다.

    그리고 벽을 이전 풀이와 다르게 구현할까 생각해봤지만, 마땅한 방식이 생각나지 않아 이전처럼 set()으로 구현했습니다.


2. 구현 (16:09 - 16:44)
    이전에는 바람 방향의 좌우/상하를 구분하지 않고, 통합적인 코드를 구현했습니다.
    그러나 이번에는, 더 확실하고 꼬이지 않게 구현할 수 있는 코드를 작성했습니다.
    이번 방식이 오타로 인한 실수의 여지가 더 크지만,
    복붙과정에서 더 꼼꼼히 검수하고, 지웠다 새로 써보는 과정을 여러번 거쳐준다면,
    실수할 여지도 거의 없앨 수 있을 것이라고 생각합니다.


3. 디버깅 (-)


4. 시간초과 (16:45 - 16:46)
    문제에서 시간이 100을 넘으면 -1을 출력하라고 했는데,
    구현에 집중하다보니, 해당 지문을 까먹었습니다.
    바로 수정해줬습니다.
"""

direction = ((0, -1), (-1, 0), (0, 1), (1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def cal_cool(oy, ox, wind_d):
    now_added_cool = [[0] * n for _ in range(n)]

    dy, dx = direction[wind_d]

    now_added_cool[oy + dy][ox + dx] = 5

    for cool_d in range(5):
        strength = 5 - cool_d

        if dx:
            center_y, center_x = oy, ox + dx * (cool_d + 1)
            for row in range(center_y - cool_d, center_y + cool_d + 1):
                now_y, now_x = row, center_x

                if oob(now_y, now_x) or not now_added_cool[now_y][now_x]:
                    continue

                now_num = now_y * n + now_x

                one_y, one_x = now_y - 1, now_x + dx
                if not oob(one_y, one_x) \
                        and (now_num, one_y * n + one_x - dx) not in walls \
                        and (one_y * n + one_x - dx, one_y * n + one_x) not in walls:
                    now_added_cool[one_y][one_x] = strength - 1

                two_y, two_x = now_y, now_x + dx
                if not oob(two_y, two_x) and (now_num, two_y * n + two_x) not in walls:
                    now_added_cool[two_y][two_x] = strength - 1

                three_y, three_x = now_y + 1, now_x + dx
                if not oob(three_y, three_x) \
                        and (now_num, three_y * n + three_x - dx) not in walls \
                        and (three_y * n + three_x - dx, three_y * n + three_x) not in walls:
                    now_added_cool[three_y][three_x] = strength - 1

        else:  # elif dy:
            center_y, center_x = oy + dy * (cool_d + 1), ox
            for col in range(center_x - cool_d, center_x + cool_d + 1):
                now_y, now_x = center_y, col

                if oob(now_y, now_x) or not now_added_cool[now_y][now_x]:
                    continue

                now_num = now_y * n + now_x

                one_y, one_x = now_y + dy, now_x - 1
                if not oob(one_y, one_x) \
                        and (now_num, (one_y - dy) * n + one_x) not in walls \
                        and ((one_y - dy) * n + one_x, one_y * n + one_x) not in walls:
                    now_added_cool[one_y][one_x] = strength - 1

                two_y, two_x = now_y + dy, now_x
                if not oob(two_y, two_x) and (now_num, two_y * n + two_x) not in walls:
                    now_added_cool[two_y][two_x] = strength - 1

                three_y, three_x = now_y + dy, now_x + 1
                if not oob(three_y, three_x) \
                        and (now_num, (three_y - dy) * n + three_x) not in walls \
                        and ((three_y - dy) * n + three_x, three_y * n + three_x) not in walls:
                    now_added_cool[three_y][three_x] = strength - 1

    for y in range(n):
        for x in range(n):
            if now_added_cool[y][x]:
                added_cool[y][x] += now_added_cool[y][x]


def check():
    for y, x in check_indexes:
        if area[y][x] < k:
            return False
    return True


def mix():
    changed = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[y][x] <= area[ny][nx] or (y * n + x, ny * n + nx) in walls:
                    continue
                value = (area[y][x] - area[ny][nx]) // 4
                changed[y][x] -= value
                changed[ny][nx] += value

    for y in range(n):
        for x in range(n):
            area[y][x] += changed[y][x]


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
wall_inputs = [list(map(int, input().split())) for _ in range(m)]

walls = set()
for aa, bb, ss in wall_inputs:
    ci, cj = aa - 1, bb - 1
    if not ss:
        ni, nj = aa - 2, bb - 1
    else:
        ni, nj = aa - 1, bb - 2
    walls.add((ci * n + cj, ni * n + nj))
    walls.add((ni * n + nj, ci * n + cj))

added_cool = [[0] * n for _ in range(n)]
check_indexes = []
for i in range(n):
    for j in range(n):
        if not area[i][j]:
            continue
        if area[i][j] == 1:
            check_indexes.append((i, j))
        elif area[i][j]:
            cal_cool(i, j, area[i][j] - 2)
        area[i][j] = 0

time = 0
while not check() and time != 101:
    time += 1

    for i in range(n):
        for j in range(n):
            area[i][j] += added_cool[i][j]

    mix()

    for i in range(n):
        if area[0][i]:
            area[0][i] -= 1
        if area[-1][i]:
            area[-1][i] -= 1
    for i in range(1, n - 1):
        if area[i][0]:
            area[i][0] -= 1
        if area[i][-1]:
            area[i][-1] -= 1

print(time if time != 101 else -1)
